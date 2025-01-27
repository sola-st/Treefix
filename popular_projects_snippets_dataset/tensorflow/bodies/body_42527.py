# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v1 = variables.Variable(2.)

def f():
    v2 = variables.Variable(3.)
    exit(array_ops.identity(v1 * v2 * constant_op.constant(1.), 'fetch'))

f_wrapped = wrap_function.wrap_function(f, [])
self.assertAllEqual(6.0, f_wrapped())

# Test pruning directly on the inputs
pruned = f_wrapped.prune(
    feeds=f_wrapped.inputs,
    fetches=f_wrapped.graph.get_tensor_by_name('fetch:0'))
self.assertAllEqual(6.0, pruned())

# Test pruning with no inputs
pruned = f_wrapped.prune(
    feeds=(),
    fetches=f_wrapped.graph.get_tensor_by_name('fetch:0'))
self.assertAllEqual(6.0, pruned())
