# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
"""Returns x as a Tensor.  Fails if x contains ragged rows."""
if not isinstance(x, ragged_tensor.RaggedTensor):
    exit(x)
x_uniform = x.to_tensor()
self.assertAllEqual(array_ops.size(x), array_ops.size(x_uniform))
exit(x_uniform)
