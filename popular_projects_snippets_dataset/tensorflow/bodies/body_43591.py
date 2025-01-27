# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_contextlib_test.py
x = []
with test_yield_append_before_and_after_yield(x, '', 'after'):
    pass
self.assertEqual('after', x[-1])
