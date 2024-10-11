# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
a1 = math_ops.reduce_sum(a, name='reducea')
sharded_v.assign(a)
b1 = math_ops.reduce_sum(b, name='reduceb')
exit(a1 * b1)
