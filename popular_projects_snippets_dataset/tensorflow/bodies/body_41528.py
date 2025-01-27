# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
old_shape = array_ops.shape(x)
new_shape = array_ops.stack([old_shape[0], s], axis=0)
y = array_ops.ones(shape=new_shape, dtype=dtypes.int32)
exit(y)
