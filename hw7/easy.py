class TreeNode:
    """Class representing a node in a binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    """Inserts a value into the binary search tree (BST)."""
    if root is None:
        return TreeNode(value)
    
    if value <= root.value:  # Allowing duplicates by placing them in the left subtree
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)

    return root

# Example Usage:
def inorder_traversal(root):
    """Helper function to do inorder traversal and print the tree."""
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Create a BST and insert values
root = None
values = [10, 5, 15, 3, 7, 12, 18]
for v in values:
    root = insert_into_bst(root, v)

# Print inorder traversal of BST
print("Inorder Traversal of BST:")
inorder_traversal(root)  



"""
# ChatGPT Prompt:
Write a Python function to insert a value into a binary search tree. The function should take the root node of the tree and the value to be inserted as parameters. It should:
- Create a new node if the tree is empty.
- Recursively traverse the tree to find the correct position.
- Insert the value while maintaining BST properties.
- Return the updated root node.
"""
