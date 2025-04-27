def tree_by_levels(node):
    if node is None:
        return []
    result = []
    stack = [node]
    while stack:
        current = stack.pop(0)
        result.append(current.value)
        l = current.left
        r = current.right
        if l:
            stack.append(l)
        if r:
            stack.append(r)
    return result