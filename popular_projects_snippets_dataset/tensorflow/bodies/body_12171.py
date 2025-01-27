# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# All these cases result in an output filled with zeros, so we don't call
# np.einsum. Also np.einsum doesn't support generalized diagonals which
# are needed for EinsumOp gradients.
r = np.random.RandomState(0)
inputs = [np.array(r.randn(*shape)) for shape in input_shapes]
input_tensors = [constant_op.constant(x, shape=x.shape) for x in inputs]
output = self.evaluate(special_math_ops.einsum(equation, *input_tensors))
self.assertAllClose(output, np.zeros(output_shape), atol=1e-4, rtol=1e-4)
