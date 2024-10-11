# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
tf_func_dec = polymorphic_function.function(
    input_signature=(tensor_spec.TensorSpec([], dtypes.int32),))
error_message = 'input_signature missing type constraint'
with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(lambda ar1, arg2, arg3: None)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(lambda arg1, arg2, arg3, **kwargs: None)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(lambda arg1, arg2, arg3, arg4=4, **kwargs: None)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(lambda arg1, arg2, arg3, *args: None)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(lambda arg1, arg2, arg3, *args, **kwargs: None)(1, 2, 3)

self.assertEqual(
    tf_func_dec(lambda arg1, arg4=4, **kwargs: arg1 + arg4)(1).numpy(), 5)
