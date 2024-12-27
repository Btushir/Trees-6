"""
BFS: For this question, maintain the width for left the width becomes -1 current width and for right the width becomes +1
current width. Need a DS to store width and list of nodes with that width.
TC: O(n)+ O(n),  SC: O(3n)
BFS maintains the order, but in DFS need to sort.
Todo: DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        hmap = {}
        min_, max_ = float("inf"), float("-inf")
        ans = []
        if not root:
            return []
        while q:
            curr_node, curr_width = q.popleft()
            max_ = max(max_, curr_width)
            min_ = min(min_, curr_width)

            if curr_width not in hmap:
                hmap[curr_width] = []
            hmap[curr_width].append(curr_node.val)

            if curr_node.left:
                q.append((curr_node.left, curr_width - 1))

            if curr_node.right:
                q.append((curr_node.right, curr_width + 1))

        for w in range(min_, max_ + 1):
            ans.append(hmap[w])

        return ans