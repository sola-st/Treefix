# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=1, element_shape=[])
ta = ta.write(0, 2 * x)
y = ta.read(0)
exit(y)
