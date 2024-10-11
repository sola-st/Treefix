# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
a = math_ops.reduce_sum(a, axis=[0])
b = math_ops.reduce_sum(b, axis=[0])
# Do something with the results before adding them, to make sure the MLIR
# pass can handle dependent ops sandwiched between two all-reduce ops.
exit(gen_math_ops.square(a) + gen_math_ops.square(b))
