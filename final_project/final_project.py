# final_project/final_project.py
import os
from datetime import datetime
import math
import json
import networkx as nx

# Load Latest Exchange Rate Files
def load_today_exchange_rates():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, 'data')
    today = datetime.now().strftime("%Y.%m.%d")
    latest_files = {}
    exchange_data = []

    for filename in os.listdir(data_dir):
        if today in filename and filename.endswith('.txt'):
            parts = filename.split('_')
            if len(parts) >= 3:
                pair_key = parts[0] + "_" + parts[1]
                file_time = parts[2].replace('.txt', '')
                if pair_key not in latest_files or file_time > latest_files[pair_key][1]:
                    latest_files[pair_key] = (filename, file_time)

    for filename, _ in latest_files.values():
        file_path = os.path.join(data_dir, filename)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) == 2:
                    from_curr, to_curr, rate = lines[1].strip().split(',')
                    exchange_data.append((from_curr, to_curr, float(rate)))
        except Exception as e:
            print("Failed to read", filename, ":", e)

    return exchange_data

# Build Graph with Log-Transformed Weights 
def build_exchange_graph(exchange_rates):
    G = nx.DiGraph()
    for from_curr, to_curr, rate in exchange_rates:
        if rate > 0:
            weight = -math.log(rate)
            G.add_edge(from_curr, to_curr, weight=weight, rate=rate)
    return G

#  Detect and Simulate All Profitable Arbitrage Cycles 
def find_and_simulate_all_arbitrage(graph, fee_percent=0.002):
    results = []
    seen_cycles = set()
    total_cycles_checked = 0
    profitable_cycles_found = 0

    try:
        all_cycles = list(nx.simple_cycles(graph))

        for cycle_nodes in all_cycles:
            cycle_tuple = tuple(cycle_nodes)
            if cycle_tuple in seen_cycles or len(cycle_nodes) < 2:
                continue
            seen_cycles.add(cycle_tuple)

            cycle_nodes.append(cycle_nodes[0])
            value = 1.0

            try:
                for i in range(len(cycle_nodes) - 1):
                    u = cycle_nodes[i]
                    v = cycle_nodes[i + 1]
                    rate = graph[u][v]['rate']
                    value *= rate * (1 - fee_percent)
            except Exception:
                continue  # Skip incomplete or broken cycles

            total_cycles_checked += 1

            if value > 1.00005:  
                profitable_cycles_found += 1

                profit_percent = (value - 1.0) * 100
                now = datetime.now().strftime("%Y-%m-%d %H:%M")

                result = {
                    "start_currency": cycle_nodes[0],
                    "cycle": cycle_nodes,
                    "final_value": round(value, 6),
                    "profit_percent": round(profit_percent, 2),
                    "detected_at": now
                }

                if profit_percent < 0.1:
                    print("Warning: Small profit cycle found:", profit_percent, "%", "Cycle:", cycle_nodes)

                results.append(result)

    except Exception as e:
        print("Error detecting cycles:", e)

    print("Total cycles checked:", total_cycles_checked)
    print("Profitable cycles found:", profitable_cycles_found)

    return results


# Save Profitable Results ===
def save_results(results):
    result_path = os.path.join(os.path.dirname(__file__), 'results.json')
    try:
        with open(result_path, 'w') as f:
            json.dump(results, f, indent=4)
        print("All profitable cycles saved to results.json")
    except Exception as e:
        print("Failed to save results.json:", e)

# === Main Runner ===
if __name__ == "__main__":
    print("Loading exchange rates...")
    rates = load_today_exchange_rates()
    print("Loaded", len(rates), "exchange rate pairs.")

    print("Building exchange rate graph...")
    graph = build_exchange_graph(rates)
    print("Graph built with", len(graph.nodes), "currencies and", len(graph.edges), "exchange paths.")

    print("Searching for all profitable arbitrage cycles...")
    profitable_cycles = find_and_simulate_all_arbitrage(graph)

    if profitable_cycles:
        print("Profitable arbitrage cycles found:", len(profitable_cycles))
        save_results(profitable_cycles)
    else:
        print("No profitable arbitrage opportunities found today.")