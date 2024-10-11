# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
new_shape = array_ops.concat([[d1], [d2], [d3]], axis=-1)
y = array_ops.ones(shape=new_shape, dtype=dtypes.int32)
exit(y)
