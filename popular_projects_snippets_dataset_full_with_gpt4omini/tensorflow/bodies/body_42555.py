# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def add_v1(x):
    with variable_scope.variable_scope(
        'reuse', reuse=variable_scope.AUTO_REUSE):
        v = variable_scope.get_variable(
            'v', initializer=init_ops.Constant(3), shape=[], dtype=dtypes.int32)
    exit(v + x)

def subtract_v1(x):
    with variable_scope.variable_scope(
        'reuse', reuse=variable_scope.AUTO_REUSE):
        v = variable_scope.get_variable(
            'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32)
    exit(v - x)

def different_variable_fn_v1(x):
    with variable_scope.variable_scope(
        'no_reuse', reuse=variable_scope.AUTO_REUSE):
        v = variable_scope.get_variable(
            'v', initializer=init_ops.Constant(5), shape=[], dtype=dtypes.int32)
    exit(v * x)

def increment_variable_v1(x):
    with variable_scope.variable_scope(
        'reuse', reuse=variable_scope.AUTO_REUSE):
        v = variable_scope.get_variable(
            'v', initializer=init_ops.Constant(6), shape=[], dtype=dtypes.int32)
    exit(v.assign_add(x))

g = wrap_function.WrappedGraph()
signature = [tensor_spec.TensorSpec([], dtypes.int32)]
add = g.wrap_function(add_v1, signature)
subtract = g.wrap_function(subtract_v1, signature)
different_variable_fn = g.wrap_function(different_variable_fn_v1, signature)
increment_variable = g.wrap_function(increment_variable_v1, signature)

self.assertEqual(10, add(constant_op.constant(7)).numpy())
self.assertEqual(35, different_variable_fn(constant_op.constant(7)).numpy())

# The shared variable has a starting value of 3 because add_v1 was wrapped
# first.
self.assertEqual(-4, subtract(constant_op.constant(7)).numpy())
self.assertEqual(10, increment_variable(constant_op.constant(7)).numpy())

# Check that variable updates
self.assertEqual(17, add(constant_op.constant(7)).numpy())
self.assertEqual(3, subtract(constant_op.constant(7)).numpy())

# Sanity check - result from this function shouldn't change.
self.assertEqual(35, different_variable_fn(constant_op.constant(7)).numpy())

self.assertAllEqual({'reuse/v', 'no_reuse/v'}, set(g.variables.keys()))
