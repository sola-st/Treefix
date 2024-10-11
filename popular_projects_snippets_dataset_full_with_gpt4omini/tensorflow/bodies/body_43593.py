# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_contextlib_test.py
x = []
with test_yield_append_before_and_after_yield(x, 1, 2):
    pass
with test_yield_append_before_and_after_yield(x, 3, 4):
    pass
self.assertEqual([1, 2, 3, 4], x)
