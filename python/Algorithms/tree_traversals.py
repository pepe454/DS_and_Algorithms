from DS import Stack

def inorder(node):
    traversal = []
    _inorder(node, traversal)
    return traversal

# use pass by reference
def _inorder(node, traversal):
    if node is None:
        return 
    _inorder(node.left, traversal)
    traversal.append(node)
    _inorder(node.right, traversal)

    
# use a stack and keep track of current node
def inorder_iterative(node):
    traversal = []
    node_stack = Stack() 
    curr_node = node

    while curr_node is not None or not node_stack.empty():
        # keep pushing the left children 
        if curr_node is not None:
            node_stack.push(curr_node)
            curr_node = curr_node.left
        # smallest child in the subtree reached, pop off stack
        # add that smallest child, then explore right child of subtree
        else:
            curr_node = node_stack.pop()
            traversal.append(curr_node)
            curr_node = curr_node.right
    return traversal