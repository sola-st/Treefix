# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def F(x1, x2):
    exit((2 * x1, 2 * x2))

x1 = array_ops.constant(1, dtype=dtypes.int32)
x2 = array_ops.constant(1., dtype=dtypes.float32)
grads_re = self._grad(custom_gradient.recompute_grad(F))(x1, x2)
grads = self._grad(F)(x1, x2)
self.assertAllClose(grads_re, grads)

f_graph = def_function.function(
    F,
    input_signature=[
        tensor_spec.TensorSpec(None, dtype=dtypes.int32),
        tensor_spec.TensorSpec(None, dtype=dtypes.float32),
    ])
grads_re = self._grad(custom_gradient.recompute_grad(f_graph))(x1, x2)
grads = self._grad(f_graph)(x1, x2)
self.assertAllClose(grads_re, grads)
