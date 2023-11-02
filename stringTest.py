def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char for char in s if char.isalnum()).lower()
    return cleaned == cleaned[::-1]

def compress_string(s: str) -> str:
    if not s: return ""
    res, count = [s[0]], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                res.append(str(count))
            res.append(s[i])
            count = 1
    if count > 1:
        res.append(str(count))
    return ''.join(res)

def first_unique_char(s: str) -> int:
    from collections import defaultdict
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1


def count_vowels_consonants(s: str) -> tuple:
    s = s.lower()
    count_v = sum(1 for char in s if char in "aeiou")
    count_c = sum(1 for char in s if char.isalpha() and char not in "aeiou")
    return count_v, count_c

def longest_common_prefix(strs: list) -> str:
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(s) and i < len(prefix) and s[i] == prefix[i]:
            i += 1
        prefix = prefix[:i]
    return prefix

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def count_substring(s: str, sub: str) -> int:
    return s.count(sub)

def title_case(s: str) -> str:
    return s.title()

def caesar_cipher(s: str, shift: int) -> str:
    result = []
    for char in s:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


import unittest


class TestStringMethods(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))
        self.assertFalse(is_palindrome("hello"))

    def test_compress_string(self):
        self.assertEqual(compress_string("aabcc"), "a2bc2")
        self.assertEqual(compress_string("aa"), "a2")
        self.assertEqual(compress_string("a"), "a")

    def test_first_unique_char(self):
        self.assertEqual(first_unique_char("leetcode"), 0)
        self.assertEqual(first_unique_char("loveleetcode"), 2)
        self.assertEqual(first_unique_char("aabb"), -1)

    def test_count_vowels_consonants(self):
        self.assertEqual(count_vowels_consonants("hello"), (2, 3))
        self.assertEqual(count_vowels_consonants("aeiou"), (5, 0))
        self.assertEqual(count_vowels_consonants("xyz"), (0, 3))

    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix([""]), "")

    def test_is_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))

    def test_count_substring(self):
        self.assertEqual(count_substring("hello hello hello", "hello"), 3)
        self.assertEqual(count_substring("abc", "d"), 0)

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("PYTHON"), "Python")
        self.assertEqual(title_case(""), "")

    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("ABC", 1), "BCD")
        self.assertEqual(caesar_cipher("z", 1), "a")
        self.assertEqual(caesar_cipher("Z", 1), "A")


if __name__ == '__main__':
    unittest.main()
