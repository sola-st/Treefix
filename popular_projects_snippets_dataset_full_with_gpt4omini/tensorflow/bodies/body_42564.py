# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def update_var_v1(x):
    v = variables.Variable(3, name='v')
    update_op = state_ops.assign(v, x).op
    exit(update_op)

g = wrap_function.WrappedGraph()
signature = [tensor_spec.TensorSpec([], dtypes.int32)]
update_var = g.wrap_function(update_var_v1, signature)

self.assertEqual(g.variables['v'].numpy(), 3)
update_var(constant_op.constant(12))
self.assertEqual(g.variables['v'].numpy(), 12)
