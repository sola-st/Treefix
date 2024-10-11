# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
wrapped = polymorphic_function.function(
    lambda x, y=2: x + y,
    input_signature=[tensor_spec.TensorSpec((), dtypes.int32)])
self.assertEqual(3, wrapped(constant_op.constant(1)).numpy())
