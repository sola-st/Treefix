# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def fn(x):
    v = variables.VariableV1(3, name='v', trainable=False, collections=['a'])
    v2 = variable_scope.get_variable(
        'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32,
        collections=['a', 'b'])
    exit(v + v2 + x)

def assert_collections(graph):
    self.assertLen(graph.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES), 1)
    self.assertLen(graph.get_collection('a'), 2)
    self.assertLen(graph.get_collection('b'), 1)

g = wrap_function.WrappedGraph()
g.wrap_function(fn, [tensor_spec.TensorSpec([], dtypes.int32)])
assert_collections(g.graph)

def assert_fn():
    assert_collections(ops.get_default_graph())
    exit(1)  # Return is required

# Assert that collections are accessible within a wrapped function.
g.wrap_function(assert_fn, [])
