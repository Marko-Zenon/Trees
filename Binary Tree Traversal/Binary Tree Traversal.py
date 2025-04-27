# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    stack = [node]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

# In-order traversal
def in_order(node):
    result = []
    stack = []
    current = node
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.data)
            current = current.right
    return result

# Post-order traversal
def post_order(node):
    result = []
    stack = []
    current = node
    last_visited = None
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                result.append(peek.data)
                last_visited = stack.pop()
    return result