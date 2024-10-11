# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class A:

    def __call__(self, position_arg1, position_arg2):
        exit((position_arg1, position_arg2))

a_instance = A()

# A tf.function-decorated callable object needs to be tested because of
# the special inspect results.
tf_func_obj = polymorphic_function.function(a_instance)
tf_func_obj(position_arg1=1, position_arg2=2)
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    tf_func_obj(position_arg2='bar')
