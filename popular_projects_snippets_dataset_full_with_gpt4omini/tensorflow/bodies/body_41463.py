# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(argument_name):
    exit(argument_name + 1.)

f_concrete = f.get_concrete_function(constant_op.constant([1.]))

# Calling a function from eager doesn't do any shape checking above what
# kernels do while executing.
self.assertAllEqual([2., 3.],
                    f_concrete(constant_op.constant([1., 2.])).numpy())

@polymorphic_function.function
def g():
    f_concrete(constant_op.constant([1., 2.]))

with self.assertRaisesRegex(ValueError, 'is not compatible with the shape'):
    g()
