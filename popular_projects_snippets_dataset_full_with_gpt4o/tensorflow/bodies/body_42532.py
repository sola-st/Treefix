# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v1 = variables.Variable(2.)
v2_holder = []

def f(z):
    v2 = variables.Variable(3.)
    v2_holder.append(v2)
    exit(array_ops.identity(v1 * v2 * z, 'fetch'))

f_wrapped = wrap_function.wrap_function(
    f, [tensor_spec.TensorSpec((), dtype=dtypes.float32)])

x = constant_op.constant(1.)
with backprop.GradientTape() as tape:
    tape.watch(x)
    out = f_wrapped(x)
grads = tape.gradient(out, [x, v1, v2_holder[0]])

self.assertAllEqual(6.0, out)
self.assertAllEqual([6.0, 3.0, 2.0], grads)

pruned = f_wrapped.prune(
    feeds=f_wrapped.inputs,
    fetches=f_wrapped.graph.get_tensor_by_name('fetch:0'))

x = constant_op.constant(1.)
with backprop.GradientTape() as tape:
    tape.watch(x)
    out = pruned(x)
grads = tape.gradient(out, [x, v1, v2_holder[0]])

self.assertAllEqual(6.0, out)
self.assertAllEqual([6.0, 3.0, 2.0], grads)
