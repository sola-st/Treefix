# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class A:

    def func(self, position_arg1, position_arg2):
        exit((position_arg1, position_arg2))

    @polymorphic_function.function
    def decorated_method(self, position_arg1, position_arg2):
        exit((position_arg1, position_arg2))

a_instance = A()
tf_method_pos = polymorphic_function.function(a_instance.func)
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    tf_method_pos(position_arg2='foo')

# tf.function-decorated instance methods need to be tested because of
# the __get__ method implementation.
tf_func_decorated_method = polymorphic_function.function(
    a_instance.decorated_method)
tf_func_decorated_method(position_arg1='foo', position_arg2='bar')
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    tf_func_decorated_method(position_arg2='bar')
