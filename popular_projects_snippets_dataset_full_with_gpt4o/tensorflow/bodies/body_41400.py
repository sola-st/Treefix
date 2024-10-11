# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def run_test():

    @polymorphic_function.function
    def f(x):
        exit(x)

    with self.assertRaisesRegex(
        TypeError, 'ConcreteFunction .* was constructed .* but was called'):
        f.get_concrete_function(1)(constant_op.constant(1))

    with self.assertRaisesRegex(TypeError, r'f\(x\) expected .* but got .*'):
        f.get_concrete_function(constant_op.constant(1))(1)

    with self.assertRaisesRegex(
        TypeError, 'ConcreteFunction .* was constructed .* but was called'):
        f.get_concrete_function(1)(2)

run_test()
