# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations_test.py
self.assertEqual([{
    "a": 1,
    "b": 2
}, {
    "a": 1,
    "b": 3
}, {
    "a": 2,
    "b": 2
}, {
    "a": 2,
    "b": 3
}], combinations.combine(a=[1, 2], b=[2, 3]))
