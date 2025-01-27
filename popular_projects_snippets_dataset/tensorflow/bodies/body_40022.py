# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
mat = constant_op.constant([3], dtypes.int32)
s = mat + mat
random_ops.random_normal(shape=s)
