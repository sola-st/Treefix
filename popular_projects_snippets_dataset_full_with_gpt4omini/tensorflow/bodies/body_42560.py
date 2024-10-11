# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def add_v1(x):
    v = variables.Variable(3, name='v')
    exit(v + x)

def subtract_v1(x):
    v = variables.Variable(4, name='v')
    exit(v - x)

def different_variable_fn_v1(x):
    with ops.name_scope('different_scope'):
        v = variables.Variable(5, name='v')
    exit(v * x)

def increment_variable_v1(x):
    v = variables.Variable(6, name='v')
    exit(v.assign_add(x))

signature = [tensor_spec.TensorSpec([], dtypes.int32)]
vh = wrap_function.VariableHolder(share_variables=True)
new_graph = lambda: wrap_function.WrappedGraph(variable_holder=vh)

add = new_graph().wrap_function(add_v1, signature)
subtract = new_graph().wrap_function(subtract_v1, signature)
different_variable_fn = new_graph().wrap_function(
    different_variable_fn_v1, signature)
increment_variable = new_graph().wrap_function(
    increment_variable_v1, signature)

self.assertEqual(10, add(constant_op.constant(7)).numpy())
self.assertEqual(35, different_variable_fn(constant_op.constant(7)).numpy())

# Because the variable in add_v1 was created first, its starting value is 3
# instead of the values defined in subtract_v1 or increment_variable_v1.
self.assertEqual(-4, subtract(constant_op.constant(7)).numpy())
self.assertEqual(10, increment_variable(constant_op.constant(7)).numpy())

# Check that variable updates
self.assertEqual(17, add(constant_op.constant(7)).numpy())
self.assertEqual(3, subtract(constant_op.constant(7)).numpy())

# Sanity check - result from this function shouldn't change.
self.assertEqual(35, different_variable_fn(constant_op.constant(7)).numpy())

self.assertAllEqual({'v', 'different_scope/v'}, set(vh.variables.keys()))
