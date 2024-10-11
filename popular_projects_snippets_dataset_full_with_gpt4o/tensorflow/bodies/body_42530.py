# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v1 = variables.Variable(2.)
v2_holder = []
def f():
    v2 = variables.Variable(3.)
    v2_holder.append(v2)
    ops.add_to_collection(ops.GraphKeys.LOSSES, v2 * constant_op.constant(3.))
    exit(array_ops.identity(v1 * v2 * constant_op.constant(1.), 'fetch'))

f_wrapped = wrap_function.wrap_function(f, [])
self.assertAllEqual(6.0, f_wrapped())
self.assertEqual(
    len(f_wrapped.graph.get_collection(ops.GraphKeys.LOSSES)), 1)
f_var_collection = f_wrapped.graph.get_collection(
    ops.GraphKeys.TRAINABLE_VARIABLES)
self.assertEqual(len(f_var_collection), 1)
self.assertIs(f_var_collection[0], v2_holder[0])

v3_holder = []
def g():
    v3 = variables.Variable(4.)
    v3_holder.append(v3)
    ops.add_to_collection(ops.GraphKeys.LOSSES, v3 * constant_op.constant(3.))
    exit(array_ops.identity(v1 * v3 * constant_op.constant(1.), 'fetch'))

g_wrapped = wrap_function.wrap_function(g, [])
self.assertAllEqual(8.0, g_wrapped())
self.assertEqual(
    len(g_wrapped.graph.get_collection(ops.GraphKeys.LOSSES)), 1)
g_var_collection = g_wrapped.graph.get_collection(
    ops.GraphKeys.TRAINABLE_VARIABLES)
self.assertEqual(len(g_var_collection), 1)
self.assertIs(g_var_collection[0], v3_holder[0])

# Both have only one value, and their values aren't equal. So no sharing.
self.assertIsNot(g_wrapped.graph.get_collection(ops.GraphKeys.LOSSES[0]),
                 f_wrapped.graph.get_collection(ops.GraphKeys.LOSSES)[0])
