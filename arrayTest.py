def reverse_array(arr):
    return arr[::-1]

def find_maximum(arr):
    return max(arr)

def find_minimum(arr):
    return min(arr)

def move_zeroes(arr):
    count = arr.count(0)
    arr = [i for i in arr if i != 0]
    arr.extend([0]*count)
    return arr

def contains_duplicate(arr):
    return len(arr) != len(set(arr))

def rotate_array(arr, k):
    k = k % len(arr)  # in case k is bigger than the array length
    return arr[-k:] + arr[:-k]

def sum_even_numbers(arr):
    return sum(i for i in arr if i % 2 == 0)

def remove_duplicates(arr):
    if not arr: return []
    index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[index] = arr[i]
            index += 1
    return arr[:index]

def merge_sorted_arrays(nums1, nums2):
    return sorted(nums1 + nums2)

def kth_max_min_element(arr, k):
    arr = sorted(arr)
    return arr[k-1], arr[-k]


import unittest


class TestArrayManipulations(unittest.TestCase):

    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_find_maximum(self):
        self.assertEqual(find_maximum([1, 2, 3, 4, 5]), 5)

    def test_find_minimum(self):
        self.assertEqual(find_minimum([1, 2, 3, 4, 5]), 1)

    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_contains_duplicate(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_rotate_array(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5, 5, 5]), [1, 2, 3, 4, 5])

    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_kth_max_min_element(self):
        self.assertEqual(kth_max_min_element([1, 2, 3, 4, 5], 2), (2, 4))


if __name__ == "__main__":
    unittest.main()
