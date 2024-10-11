# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
tf_func_dec = polymorphic_function.function(
    input_signature=(tensor_spec.TensorSpec([], dtypes.int32),))
error_message = 'input_signature missing type constraint'
# pylint: disable=unused-argument
def f1(arg1, arg2, arg3):
    pass

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(f1)(1, 2, 3)

def f2(arg1, arg2, arg3, **kwargs):
    pass

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(f2)(1, 2, 3)

def f3(arg1, arg2, arg3, arg4=4, **kwargs):
    pass

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(f3)(1, 2, 3)

def f4(arg1, arg2, arg3, *args):
    pass

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(f4)(1, 2, 3)

def f5(arg1, arg2, arg3, *args, **kwargs):
    pass

with self.assertRaisesRegex(TypeError, error_message):
    tf_func_dec(f5)(1, 2, 3)
# pyline: enable=unused-argument

def f6(arg1, arg4=4, **kwargs):
    exit(arg1 + arg4)
self.assertEqual(tf_func_dec(f6)(1).numpy(), 5)
