# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        stack = [(None, root, False)]
        while stack:
            parent, current, is_left = stack.pop()
            if not current:
                continue
            if current.val == key:
                if not current.left and not current.right:
                    if not parent:
                        return None
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None

                elif not current.left:
                    if not parent:
                        return current.right
                    if is_left:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                elif not current.right:
                    if not parent:
                        return current.left
                    if is_left:
                        parent.left = current.left
                    else:
                        parent.right = current.left

                else:
                    succ_parent = current
                    succ = current.right
                    while succ.left:
                        succ_parent = succ
                        succ = succ.left
                    current.val = succ.val
                    if succ_parent.left == succ:
                        succ_parent.left = succ.right
                    else:
                        succ_parent.right = succ.right
                break
            if key < current.val:
                stack.append((current, current.left, True))
            else:
                stack.append((current, current.right, False))

        return root
