# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class MyModule(module.Module):

    def f1(self, arg1, arg2, arg3):
        pass

    def f2(self, arg1, arg2, arg3, **kwargs):
        pass

    def f3(self, arg1, arg2, arg3, arg4=4, **kwargs):
        pass

    def f4(self, arg1, arg2, arg3, *args):
        pass

    def f5(self, arg1, arg2, arg3, *args, **kwargs):
        pass

    def f6(self, arg1, arg4=4, **kwargs):
        exit(arg1 + arg4)

m = MyModule()
tf_func_dec = polymorphic_function.function(
    input_signature=(tensor_spec.TensorSpec([], dtypes.int32),))
error_message = 'input_signature missing type constraint'
with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(m.f1)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(m.f2)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(m.f3)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(m.f4)(1, 2, 3)

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(m.f5)(1, 2, 3)

self.assertEqual(tf_func_dec(m.f6)(1).numpy(), 5)
