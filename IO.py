def read_numbers_from_file(filename="numbers.txt"):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

def write_strings_to_file(strings, filename="strings.txt"):
    with open(filename, "w") as file:
        for s in strings:
            file.write(s + "\n")

def read_kv_from_file(filename="kv.txt"):
    with open(filename, "r") as file:
        return {line.split(",")[0]: line.split(",")[1].strip() for line in file}

def append_numbers_to_file(numbers, filename="numbers.txt"):
    with open(filename, "a") as file:
        for num in numbers:
            file.write(str(num) + "\n")

import csv

def read_csv_to_dict(filename="data.csv"):
    with open(filename, "r") as file:
        return list(csv.DictReader(file))

import json

def write_dict_to_json(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file)

def read_json_to_dict(filename="data.json"):
    with open(filename, "r") as file:
        return json.load(file)

def copy_file_content(source="source.txt", destination="destination.txt"):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())

def read_every_nth_line(n, filename="lines.txt"):
    with open(filename, "r") as file:
        return [line for index, line in enumerate(file, 1) if index % n == 0]


import unittest
import os
import json

class TestIOFunctions(unittest.TestCase):

    def test_read_numbers_from_file(self):
        with open('test_numbers.txt', 'w') as f:
            f.write("1\n2\n3")
        result = read_numbers_from_file('test_numbers.txt')
        os.remove('test_numbers.txt')
        self.assertEqual(result, [1, 2, 3])

    def test_write_strings_to_file(self):
        write_strings_to_file(['a', 'b', 'c'], 'test_strings.txt')
        with open('test_strings.txt', 'r') as f:
            content = f.read()
        os.remove('test_strings.txt')
        self.assertEqual(content, 'a\nb\nc\n')

    def test_read_kv_from_file(self):
        with open('test_kv.txt', 'w') as f:
            f.write("key,value\nkey2,value2")
        result = read_kv_from_file('test_kv.txt')
        os.remove('test_kv.txt')
        self.assertEqual(result, {'key': 'value', 'key2': 'value2'})

    def test_append_numbers_to_file(self):
        with open('test_numbers_append.txt', 'w') as f:
            f.write("1\n2\n3\n")
        append_numbers_to_file([4, 5], 'test_numbers_append.txt')
        with open('test_numbers_append.txt', 'r') as f:
            content = f.read()
        os.remove('test_numbers_append.txt')
        self.assertEqual(content, '1\n2\n3\n4\n5\n')

    def test_read_csv_to_dict(self):
        with open('test_data.csv', 'w') as f:
            f.write("col1,col2\nval1,val2")
        result = read_csv_to_dict('test_data.csv')
        os.remove('test_data.csv')
        self.assertEqual(result, [{'col1': 'val1', 'col2': 'val2'}])

    def test_write_dict_to_json(self):
        data = [{"key": "value"}]
        write_dict_to_json(data, 'test_data.json')
        with open('test_data.json', 'r') as f:
            content = json.load(f)
        os.remove('test_data.json')
        self.assertEqual(content, data)

    def test_read_json_to_dict(self):
        data = {"key": "value"}
        with open('test_data_read.json', 'w') as f:
            json.dump(data, f)
        result = read_json_to_dict('test_data_read.json')
        os.remove('test_data_read.json')
        self.assertEqual(result, data)

    def test_copy_file_content(self):
        with open('test_source.txt', 'w') as f:
            f.write("content")
        copy_file_content('test_source.txt', 'test_dest.txt')
        with open('test_dest.txt', 'r') as f:
            content = f.read()
        os.remove('test_source.txt')
        os.remove('test_dest.txt')
        self.assertEqual(content, "content")

    def test_read_every_nth_line(self):
        with open('test_lines.txt', 'w') as f:
            f.write("1\n2\n3\n4\n5")
        result = read_every_nth_line(2, 'test_lines.txt')
        os.remove('test_lines.txt')
        self.assertEqual(result, ["2\n", "4\n"])

if __name__ == "__main__":
    unittest.main()
