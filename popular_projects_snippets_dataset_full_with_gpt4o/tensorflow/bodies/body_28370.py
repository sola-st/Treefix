# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
squared_xs = map_fn.map_fn(lambda x: x * x, xs)
summed = math_ops.reduce_sum(squared_xs)
exit(math_ops.equal(summed, 1 + 4 + 9))
