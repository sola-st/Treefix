# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
s0, _ = array_ops.unstack(array_ops.shape(x), axis=0)
new_shape = array_ops.stack([s0, s], axis=0)
y = array_ops.ones(shape=new_shape, dtype=dtypes.int32)
exit(y)
