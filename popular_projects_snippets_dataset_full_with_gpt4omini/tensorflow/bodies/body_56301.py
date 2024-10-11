# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations_test.py
self.assertEqual([
    OrderedDict([("aa", 1), ("ab", 2)]),
    OrderedDict([("aa", 1), ("ab", 3)]),
    OrderedDict([("aa", 2), ("ab", 2)]),
    OrderedDict([("aa", 2), ("ab", 3)])
], combinations.combine(ab=[2, 3], aa=[1, 2]))
