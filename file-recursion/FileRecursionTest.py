import unittest
from FileRecursion import find_files


class FileRecursionTest(unittest.TestCase):

    def test_file_recursion(self):
        file_paths = find_files(".c", ".")
        self.assertEqual(4, len(file_paths))
        self.assertIn('./testdir/subdir3/subsubdir1/b.c', file_paths)
        self.assertIn('./testdir/t1.c', file_paths)
        self.assertIn('./testdir/subdir5/a.c', file_paths)
        self.assertIn('./testdir/subdir1/a.c', file_paths)