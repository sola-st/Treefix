# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=2, element_shape=[3])
ta = ta.write(0, 2 * x)
ta = ta.write(1, 3 * x)
exit(ta.concat())
