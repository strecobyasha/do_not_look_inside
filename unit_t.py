import unittest
from collections import Counter


def unique_characters(original_str):
    """
    Implement an algorithm to determine if a string has all unique characters.
    """
    try:
        return len(set(original_str)) == len(original_str)
    except TypeError:
        return False


def string_permutation(str1, str2):
    """
    Determine if a string is a permutation of another string.
    """
    return Counter(str1) == Counter(str2) and len(Counter(str1)) > 0


def str_rotation(str1, str2):
    """
    Determine if a string s1 is a rotation of another string s2,
    by calling (only once) a function is_substring.
    """
    try:
        return str1 in str2*2 and len(str1) == len(str2)
    except TypeError:
        return False


def compress_str(original_str):
    """
    Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
    Only compress the string if it saves space.
    """
    if original_str == None or not original_str:
        return original_str
    compressed_str = ''
    current_symbol = ''
    counter = 1
    for symbol in original_str:
        if symbol != current_symbol:
            compressed_str += (str(counter) if counter > 1 else '') + symbol
            current_symbol = symbol
            counter = 1
        else:
            counter += 1
    if counter > 1:
        compressed_str += str(counter)
    if len(compressed_str) < len(original_str):
        return compressed_str
    return original_str


def reverse_str(original_string):
    """
    Implement a function to reverse a string (a list of characters), in-place.
    """
    try:
        chars = list(original_string)
        for i in range(len(chars) // 2):
            chars[i], chars[-1-i] = chars[-1-i], chars[i]
        return ''.join(chars) if isinstance(original_string, str) else chars
    except TypeError:
        return original_string


def str_difference(str1, str2):
    """
    Find the single different char between two strings.
    """
    if str1 == None or str2 == None:
        return None
    str1_dict = Counter(str1)
    str2_dict = Counter(str2)
    long_dict, short_dict = str1_dict, str2_dict
    if len(str2_dict) > len(str1_dict):
        long_dict, short_dict = str2_dict, str1_dict
    for k, v in long_dict.items():
        if k not in short_dict or short_dict[k] != v:
            return k


def indices(*args):
    """
    Given an array, find the two indices that sum to a specific value.
    """
    if len(args) != 2 or None in args:
        raise TypeError('Type error!')
    elif args[0] == []:
        raise ValueError('Value error!')
    else:
        arr = args[0]
        val = args[1]
        x_ind = 0
        for x in arr:
            y = val - x
            if y in arr[x_ind+1:]:
                return [x_ind, arr.index(y)]
            x_ind += 1


class HashTable:

    def __init__(self, size):
        self.ht = {k: 0 for k in range(size)}

    def get(self, key):
        if key in self.ht:
            return self.ht[key]
        raise KeyError('No matching key for getting')

    def set(self, key, val):
        if key not in self.ht:
            self.ht[key] = val
        self.ht[key] = val

    def remove(self, key):
        if key in self.ht:
            del self.ht[key]
            return
        raise KeyError('No matching key for removing')


class Test(unittest.TestCase):

    def test_unique_chars(self, func=unique_characters):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')

    def test_str_permutation(self, func=string_permutation):
        self.assertEqual(func(None, 'dog'), False)
        self.assertEqual(func(None, None), False)
        self.assertEqual(func('', ''), False)
        self.assertEqual(func('', 'dog'), False)
        self.assertEqual(func('Nib', 'bin'), False)
        self.assertEqual(func('act', 'cat'), True)
        self.assertEqual(func('a ct', 'ca t'), True)
        print('Success: test_str_permutation')

    def test_str_rotation(self, func=str_rotation):
        self.assertEqual(func('fooo', 'foo'), False)
        self.assertEqual(func(None, 'foo'), False)
        self.assertEqual(func('', ''), True)
        self.assertEqual(func('foobarbaz', 'barbazfoo'), True)
        print('Success: test_str_rotation')

    def test_compress_str(self, func=compress_str):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDD'), 'A3BC2D4')
        print('Success: test_compress_str')

    def test_reverse_str(self, func=reverse_str):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('word'), 'drow')
        self.assertEqual(func(['f', 'o', 'o', ' ', 'b', 'a', 'r']), ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_str')

    def test_str_difference(self, func=str_difference):
        self.assertEqual(func(None, ''), None)
        self.assertEqual(func('ab', 'aab'), 'a')
        self.assertEqual(func('aab', 'ab'), 'a')
        self.assertEqual(func('abcd', 'abcde'), 'e')
        self.assertEqual(func('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_str_difference')

    def test_indices(self, func=indices):
        self.assertRaises(TypeError, func, None, None)
        self.assertRaises(ValueError, func, [], 0)
        self.assertEqual(func([1, 3, 2, -7, 5], 7), [2, 4])
        print('Success: test_indecies')

    def test_hash_tab(self):
        hash_table = HashTable(5)
        self.assertRaises(KeyError, hash_table.get, 5)
        hash_table.set(5, 'foo')
        self.assertEqual(hash_table.get(5), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(5), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(5), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')
        hash_table.remove(10)
        self.assertEqual(hash_table.get(5), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)
        self.assertRaises(KeyError, hash_table.remove, -1)
        print('Success: test_hash_tab')


if __name__ == '__main__':
    unittest.main()
