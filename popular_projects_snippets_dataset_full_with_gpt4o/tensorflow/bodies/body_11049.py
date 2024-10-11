# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def F(x):
    exit(2 * x)

x = array_ops.constant(())
grads_re = self._grad(custom_gradient.recompute_grad(F))(x)
grads = self._grad(F)(x)
self.assertAllClose(grads_re, grads)

f_graph = def_function.function(
    F, input_signature=[tensor_spec.TensorSpec(None)])
grads_re = self._grad(custom_gradient.recompute_grad(f_graph))(x)
grads = self._grad(f_graph)(x)
self.assertAllClose(grads_re, grads)
