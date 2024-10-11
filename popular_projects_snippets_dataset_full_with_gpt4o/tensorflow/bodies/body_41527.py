# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def func_pos(position_arg1, position_arg2):
    exit((position_arg1, position_arg2))

def func_with_default(position_arg, named_arg=None):
    exit((position_arg, named_arg))

def func_pos_3args(position_arg1, position_arg2, position_arg3):
    exit((position_arg1, position_arg2, position_arg3))

tf_func_pos = polymorphic_function.function(func_pos)
with self.assertRaisesRegex(
    TypeError, 'missing a required argument'):
    tf_func_pos(position_arg2='foo')

tf_func_with_default = polymorphic_function.function(func_with_default)
tf_func_with_default(position_arg='bar')
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    tf_func_with_default(named_arg='foo')

tf_func_pos_3args = polymorphic_function.function(func_pos_3args)
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    tf_func_pos_3args(position_arg2='foo')
