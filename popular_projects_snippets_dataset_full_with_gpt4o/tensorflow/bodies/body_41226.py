# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def second(dup_var, dup_var_2, some_const):
    exit(dup_var + dup_var_2 + some_const)

@polymorphic_function.function
def first(dup_var, some_const):
    exit(second(dup_var, dup_var, some_const))

my_const = constant_op.constant(1)
my_var = variables.Variable(2, dtype=dtypes.int32)
self.assertEqual(second(my_var, my_var, my_const).numpy(), 5)
self.assertEqual(first(my_var, my_const).numpy(), 5)
