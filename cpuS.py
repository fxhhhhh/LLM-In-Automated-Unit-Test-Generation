def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def rotate(nums: list, k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

def generate_primes(n: int) -> list:
    sieve = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i: n: i] = [False] * len(range(i*i, n, i))
    return [i for i in range(2, n) if sieve[i]]

def matrix_multiply(A: list, B: list) -> list:
    return [[sum(a*b for a, b in zip(rowA, colB)) for colB in zip(*B)] for rowA in A]

def max_sub_array(nums: list) -> int:
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge_two_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_lists(l1, l2.next)
        return l2

def binary_search(arr: list, x: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


import unittest


class TestFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)

    def test_rotate(self):
        nums = [1, 2, 3, 4, 5]
        rotate(nums, 2)
        self.assertEqual(nums, [4, 5, 1, 2, 3])

    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])

    def test_matrix_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 3]]
        self.assertEqual(matrix_multiply(A, B), [[4, 6], [10, 12]])

    def test_max_sub_array(self):
        self.assertEqual(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_invert_tree(self):
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        inverted_tree = invert_tree(tree)
        self.assertEqual(inverted_tree.left.val, 3)
        self.assertEqual(inverted_tree.right.val, 2)

    def test_merge_two_sorted_lists(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        merged = merge_two_sorted_lists(l1, l2)
        self.assertEqual([merged.val, merged.next.val, merged.next.next.val, merged.next.next.next.val,
                          merged.next.next.next.next.val], [1, 1, 2, 3, 4])

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_quick_sort(self):
        self.assertEqual(quick_sort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
