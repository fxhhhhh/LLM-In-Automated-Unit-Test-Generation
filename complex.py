class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    def helper(node):
        if node:
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)
        else:
            vals.append('#')
    vals = []
    helper(root)
    return ' '.join(vals)

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Move key to end to show that it was recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first item if over capacity


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


def merge_k_sorted_lists(lists):
    dummy = ListNode(0)
    current = dummy
    heap = [(lst.val, i) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, idx = heapq.heappop(heap)
        current.next = ListNode(val)
        current = current.next

        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(heap, (lists[idx].val, idx))

    return dummy.next

class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word):
        return self._search_in_node(word, self.trie)

    def _search_in_node(self, word, node):
        for i, char in enumerate(word):
            if char in node:
                node = node[char]
            else:
                if char == '.':
                    for child in node:
                        if child != '#' and self._search_in_node(word[i+1:], node[child]):
                            return True
                return False
        return '#' in node

class Autocomplete:
    def __init__(self, sentences):
        self.trie = {}
        for sentence in sentences:
            self._insert(sentence)

    def _insert(self, sentence):
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = sentence

    def search(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return self._find_sentences(node)

    def _find_sentences(self, node):
        sentences = []
        for char, child_node in node.items():
            if char == '#':
                sentences.append(child_node)
            else:
                sentences.extend(self._find_sentences(child_node))
        return sentences

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
import heapq

def kth_largest_element(nums, k):
    return heapq.nlargest(k, nums)[-1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


def merge_k_sorted_lists(lists):
    dummy = ListNode(0)
    current = dummy
    heap = [(lst.val, i) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, idx = heapq.heappop(heap)
        current.next = ListNode(val)
        current = current.next

        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(heap, (lists[idx].val, idx))

    return dummy.next

# 1. Non-Repeated Character
def first_non_repeated(s: str) -> str:
    count_map = {}
    for c in s:
        count_map[c] = count_map.get(c, 0) + 1
    for c in s:
        if count_map[c] == 1:
            return c
    return '\0'

# 2. Object-Oriented Paradigm
class BankAccount:
    def __init__(self, initial_balance: float):
        self.balance = initial_balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self) -> float:
        return self.balance

# 3. Recursive Functions
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 4. Functions with Varied Parameters
def find_max(*numbers: int) -> int:
    return max(numbers)

# 5. Exception Handling
def read_file(filename: str) -> str:
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

# 6. Multithreading and Concurrency
import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def get_count(self) -> int:
        return self.count

# 7. Libraries and Dependencies
from datetime import datetime

def parse_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        return None

# 8. Whole Project Conversion
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self):
        return self.books

# 9. Functional Paradigm
def filter_and_square(numbers: list) -> list:
    return [n * n for n in numbers if n % 2 == 0]

import unittest

class TestTreeNodeMethods(unittest.TestCase):
    def test_serialize_and_deserialize(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        serialized = serialize(root)
        deserialized = deserialize(serialized)
        self.assertEqual(deserialized.val, 1)
        self.assertEqual(deserialized.left.val, 2)
        self.assertEqual(deserialized.right.val, 3)
        self.assertEqual(deserialized.right.left.val, 4)
        self.assertEqual(deserialized.right.right.val, 5)

class TestLRUCacheMethods(unittest.TestCase):
    def test_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

class TestMergeKSortedLists(unittest.TestCase):
    def test_merge(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        merged = merge_k_sorted_lists([l1, l2, l3])
        self.assertEqual([merged.val, merged.next.val, merged.next.next.val, merged.next.next.next.val], [1, 1, 2, 3])


class TestAutocomplete(unittest.TestCase):
    def test_search(self):
        ac = Autocomplete(["apple", "app", "banana", "bat"])
        self.assertEqual(ac.search("app"), ["apple", "app"])
        self.assertEqual(ac.search("bat"), ["bat"])
        self.assertEqual(ac.search("xyz"), [])

class TestTrie(unittest.TestCase):
    def test_operations(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))

class TestKthLargest(unittest.TestCase):
    def test_kth_largest(self):
        self.assertEqual(kth_largest_element([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(kth_largest_element([3, 2, 1], 2), 2)

class TestMergeKSortedLists(unittest.TestCase):
    # Note: Create some ListNode chains and test the function. Here's a basic test:

    def test_merge(self):
        l1 = ListNode(1, ListNode(4, ListNode(7)))
        l2 = ListNode(2, ListNode(5, ListNode(8)))
        merged = merge_k_sorted_lists([l1, l2])
        values = []
        while merged:
            values.append(merged.val)
            merged = merged.next
        self.assertEqual(values, [1, 2, 4, 5, 7, 8])

class TestNonRepeated(unittest.TestCase):
    def test_first_non_repeated(self):
        self.assertEqual(first_non_repeated("geeksforgeeks"), "f")
        self.assertEqual(first_non_repeated("aabbcc"), '\0')

class TestBankAccount(unittest.TestCase):
    def test_bank_account(self):
        account = BankAccount(100)
        self.assertTrue(account.withdraw(50))
        self.assertFalse(account.withdraw(200))
        self.assertEqual(account.get_balance(), 50)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(1, 2, 3, 4), 4)
        self.assertEqual(find_max(-1, -2, -3, -4), -1)

class TestReadFile(unittest.TestCase):
    # Note: You'll need to have a test file or mock it for this test

    def test_read_file(self):
        # Mocking file reading could be complex. A simple approach:
        self.assertEqual(read_file("non_existent_file.txt"), "File not found!")

class TestCounter(unittest.TestCase):
    def test_counter(self):
        counter = Counter()
        counter.increment()
        counter.increment()
        self.assertEqual(counter.get_count(), 2)

class TestParseDate(unittest.TestCase):
    def test_parse_date(self):
        self.assertEqual(parse_date("01/01/2020"), datetime.strptime("01/01/2020", "%d/%m/%Y"))
        self.assertEqual(parse_date("01-01-2020"), None)

class TestBookLibrary(unittest.TestCase):
    def test_library(self):
        library = Library()
        book = Book("Book Title", "Author Name")
        library.add_book(book)
        self


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("The Great Gatsby", "F. Scott Fitzgerald")

    def test_get_title(self):
        self.assertEqual(self.book.get_title(), "The Great Gatsby")

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), "F. Scott Fitzgerald")


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.book2 = Book("Moby Dick", "Herman Melville")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.get_books())

    def test_get_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertEqual(self.library.get_books(), [self.book1, self.book2])

class TestFilterAndSquare(unittest.TestCase):

    def test_filter_and_square(self):
        self.assertEqual(filter_and_square([1, 2, 3, 4]), [4, 16])
        self.assertEqual(filter_and_square([1, 3, 5]), [])
        self.assertEqual(filter_and_square([2, 4, 6, 8]), [4, 16, 36, 64])
        self.assertEqual(filter_and_square([]), [])

if __name__ == "__main__":
    unittest.main()

