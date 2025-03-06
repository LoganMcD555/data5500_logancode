class TreeNode:
    """Represents a node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = self.right = None  # Initialize left and right child as None

def insert(root, value):
    """
    Inserts a value into the BST while maintaining BST properties.
    If the tree is empty, creates a new node.
    """
    if not root:
        return TreeNode(value)  # Create a new node if root is None
    if value < root.value:
        root.left = insert(root.left, value)  # Insert in left subtree
    else:
        root.right = insert(root.right, value)  # Insert in right subtree
    return root  # Return the root node

def search(root, value):
    """
    Searches for a value in the BST.
    Returns True if found, otherwise False.
    """
    if not root or root.value == value:
        return bool(root)  # Return True if value is found, False otherwise
    return search(root.left, value) if value < root.value else search(root.right, value)  # Search in left or right subtree

def inorder(root):
    """Performs an inorder traversal of the BST (prints values in sorted order)."""
    if root:
        inorder(root.left)  # Visit left subtree
        print(root.value, end=" ")  # Print current node
        inorder(root.right)  # Visit right subtree

if __name__ == "__main__":
    # Initialize BST and insert values
    root = None
    for v in [10, 5, 15, 3, 7, 12, 18]:
        root = insert(root, v)

    # Print BST elements in sorted order
    print("Inorder Traversal:")
    inorder(root)
    print("\n")

    # Test search function
    for val in [7, 12, 20]:  # Check if these values exist in the BST
        print(f"Search {val}: {search(root, val)}")



"""
# ChatGPT Prompt:
Write a Python function to search for a value in a binary search tree. The function should:
- Take the root node and the value to search as parameters.
- Return True if the value exists in the BST, False otherwise.
- Use recursion to traverse the tree efficiently.
"""
