# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if func_type == 'method':
    class MyModule(module.Module):

        def f(self, arg1, arg2, arg3, arg4=4):
            exit(arg1 + arg2 + arg3 + arg4)
    f = MyModule().f
elif func_type == 'function':
    def f(arg1, arg2, arg3, arg4=4):
        exit(arg1 + arg2 + arg3 + arg4)
else:  # lambda_function
    f = lambda arg1, arg2, arg3, arg4=4: arg1 + arg2 + arg3 + arg4

error_message = 'input_signature missing type constraint'
tf_func_dec = polymorphic_function.function(
    input_signature=(tensor_spec.TensorSpec([], dtypes.int32),)
)
with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(functools.partial(f, 1))(2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(functools.partial(f, arg4=5))(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(functools.partial(f, 1, arg4=5))(2, 3)

self.assertAllEqual(
    tf_func_dec(functools.partial(f, 1, 2, arg4=5))(3),
    array_ops.constant(11),
)
