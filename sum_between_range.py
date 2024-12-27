"""
BFS: O(n)
DFS: O(n)

Todo: iterative inorder condition based and post order iterative
iterative pre-order: change queue with stack in the level order traversal
"""



from collections import deque
class Solution_bfs:

    def bfs(self, node, low, high):
        q = deque()
        q.append(node)

        while q:

            curr_node = q.popleft()

            if curr_node.val >= low and curr_node.val <= high:
                self.res += curr_node.val

            if curr_node.right:
                q.append(curr_node.right)

            if curr_node.left:
                q.append(curr_node.left)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.bfs(root, low, high)
        return self.res


class Solution_bfs_otpimized:

    def bfs(self, node, low, high):
        q = deque()
        q.append(node)

        while q:

            curr_node = q.popleft()

            if curr_node.val >= low and curr_node.val <= high:
                self.res += curr_node.val

            # the right node is added if current node vale is less than high
            if curr_node.right and curr_node.val < high:
                q.append(curr_node.right)

            # the left node is added if current node vale is greater than low
            if curr_node.left and curr_node.val > low:
                q.append(curr_node.left)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.bfs(root, low, high)
        return self.res



class Solution_dfs_void_based:
    def dfs(self, node, low, high):
        # base case
        if not node:
            return

            # logic
        if node.val >= low and node.val <= high:
            self.res += node.val
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.dfs(root, low, high)
        return self.res


class Solution_dfs_condition_based:
        def dfs(self, node, low, high):
            # base case
            if not node:
                return

                # logic
            if node.val >= low and node.val <= high:
                self.res += node.val

            if node.val > low:
                self.dfs(node.left, low, high)

            if node.val < high:
                self.dfs(node.right, low, high)

        def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            self.res = 0
            self.dfs(root, low, high)
            return self.res



class Solution_dfs_condition_based:
    def dfs(self, node, low, high):
        # base case
        if not node:
            # do not simply return, return 0
            return 0

        # logic
        res = 0
        if node.val >= low and node.val <= high:
            res += node.val

        if node.val > low:
            res += self.dfs(node.left, low, high)

        if node.val < high:
            res += self.dfs(node.right, low, high)

        return res

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_iterative_inorder:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        res = 0
        # do not put root inside stack
        # to process it in inorder
        while (root or stack):
            # traverse the left child, the conditon should be root not root.left
            # because initially stack is empty
            while root:
                stack.append(root)
                root = root.left

            # process the node, this is inorder
            root = stack.pop()
            if root.val >= low and root.val <= high:
                res += root.val

            root = root.right

        return res



