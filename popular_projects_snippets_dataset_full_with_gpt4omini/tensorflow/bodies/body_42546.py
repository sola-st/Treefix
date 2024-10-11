# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def fn(x):
    v = variables.Variable(3, name='v')
    v2 = variable_scope.get_variable(
        'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32)
    exit(v + v2 + x)

with self.cached_session() as sess:
    result = fn(constant_op.constant(5))
    sess.run(variables.global_variables_initializer())
    expected = sess.run(result)

g = wrap_function.WrappedGraph()
signature = [tensor_spec.TensorSpec([], dtypes.int32)]
wrapped_fn = g.wrap_function(fn, signature)
self.assertEqual(expected, wrapped_fn(constant_op.constant(5)).numpy())
