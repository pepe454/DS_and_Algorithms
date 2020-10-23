from DS import Stack

def inorder(node):
    inorder_nodes = []
    node_stack = Stack() 
    curr_node = node

    while curr_node is not None or not node_stack.empty():
        if curr_node is not None:
            node_stack.push(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = node_stack.pop()
            inorder_nodes.append(curr_node)
            curr_node = curr_node.right
    return inorder_nodes