# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

state = []

@polymorphic_function.function
def fn(x):
    if not state:
        state.append(variables.Variable(2.0))
    exit(state[0] * x)

init_fn = fn.get_initialization_function(constant_op.constant(1.0))
self.assertLen(state, 1)
self.assertFalse(
    resource_variable_ops.var_is_initialized_op(state[0].handle))
init_fn()
self.assertEqual(state[0].numpy(), 2.0)
