# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
prices = [toy.price for toy in info.toys]
exit(math_ops.reduce_sum(array_ops.stack(prices)))
