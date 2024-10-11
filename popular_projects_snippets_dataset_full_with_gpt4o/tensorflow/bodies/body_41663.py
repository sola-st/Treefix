# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def func(x):
    exit(2 * x)

func_a = func.get_concrete_function(constant_op.constant(2.))
func_b = func.get_concrete_function(constant_op.constant(2.))

self.assertIs(func_a, func_b)

with save_context.save_context(
    save_options.SaveOptions(experimental_variable_policy=save_options
                             .VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES)):
    func_c = func.get_concrete_function(constant_op.constant(2.))

with save_context.save_context(
    save_options.SaveOptions(
        experimental_variable_policy=save_options.VariablePolicy.NONE)):
    func_d = func.get_concrete_function(constant_op.constant(2.))

self.assertIsNot(func_a, func_c)
self.assertIsNot(func_a, func_d)
