class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def is_symmetric(root):
    def check(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

    return check(root, root)

def merge_trees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1

def has_path_sum(root, sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def lowest_common_ancestor(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

import unittest

class TestTreeFunctions(unittest.TestCase):

    def test_inorder_traversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(inorder_traversal(root), [1,3,2])

    def test_preorder_traversal(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(preorder_traversal(root), [1,2])

    def test_postorder_traversal(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(postorder_traversal(root), [2,3,1])

    def test_max_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(max_depth(root), 3)

    def test_is_symmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertTrue(is_symmetric(root))

        root.right.right = TreeNode(3)
        self.assertFalse(is_symmetric(root))

    def test_merge_trees(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(3)
        t1.right = TreeNode(2)

        t2 = TreeNode(2)
        t2.left = TreeNode(1)
        t2.right = TreeNode(3)

        merged_tree = merge_trees(t1, t2)
        self.assertEqual(inorder_traversal(merged_tree), [4,5,5])

    def test_has_path_sum(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        self.assertTrue(has_path_sum(root, 22))

    def test_invert_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        inverted = invert_tree(root)
        self.assertEqual(inorder_traversal(inverted), [9,7,6,4,3,2,1])

    def test_lowest_common_ancestor(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        self.assertEqual(lowest_common_ancestor(root, root.left, root.right).val, 6)

    def test_sorted_array_to_bst(self):
        nums = [-10,-3,0,5,9]
        root = sorted_array_to_bst(nums)
        self.assertEqual(preorder_traversal(root), [0,-10,-3,9,5])

if __name__ == '__main__':
    unittest.main()
