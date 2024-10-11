# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_contextlib_test.py
x = []
with test_yield_append_before_and_after_yield(x, 'before', 'after'):
    with test_yield_append_before_and_after_yield(x, 'inner', 'outer'):
        with test_yield_return_x_plus_1(1) as var:
            x.append(var)
self.assertEqual(['before', 'inner', 2, 'outer', 'after'], x)
