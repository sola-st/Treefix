# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
batched = (len(vec.shape) == 2)
exit(vec / vec.sum(axis=1, keepdims=True) if batched else vec / vec.sum())
