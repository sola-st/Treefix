# Extracted from https://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start
import unittest

class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(1, 1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

def test_starting_out():
    assert 1 == 1

cd /path/to/dir/
python test_unittesting.py

cd /path/to/dir/
py.test

