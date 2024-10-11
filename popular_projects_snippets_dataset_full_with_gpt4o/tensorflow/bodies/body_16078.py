# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
"""Tests that ragged_gather generates the right gradient.

    Args:
      params: The `params` that should be passed to `gather`.
      indices: The `indices` that should be passed to `gather`.
      expected_out: The expected value of `gather(params, indices)`.
        `expected_out.shape = indices.shape + params.shape[1:]`.
      out_grad: The value that should be fed in as the gradient for `out`
        when testing the gradient of `ragged_gather`.  Must have the same
        shape as `expected_out`.
      expected_grad: The expected gradient for that should be returned for
        `params`.  Must have hte same shape as `params`.
      params_ragged_rank: The ragged_rank of `params`.
    """
if context.executing_eagerly():
    exit()

params = ragged_factory_ops.constant(
    params, dtype=dtypes.float32, ragged_rank=params_ragged_rank)
indices = constant_op.constant(indices, dtype=dtypes.int32)
out_ragged_rank = params.ragged_rank + indices.shape.ndims - 1
out_grad = ragged_factory_ops.constant(
    out_grad, dtype=dtypes.float32, ragged_rank=out_ragged_rank)
expected_out = ragged_factory_ops.constant(
    expected_out, dtype=dtypes.float32, ragged_rank=out_ragged_rank)
expected_grad = ragged_factory_ops.constant(
    expected_grad,
    dtype=dtypes.float32,
    ragged_rank=params.ragged_rank)

out = ragged_gather_ops.gather(params, indices)
self.assertAllClose(out, expected_out)

grads = gradients_impl.gradients(
    out.flat_values,
    (params.nested_row_splits + (params.flat_values, indices,)),
    out_grad.flat_values)
param_nested_splits_grads = grads[:-2]
params_flat_values_grad = grads[-2]
indices_grad = grads[-1]
self.assertEqual(indices_grad, None)
for splits_grad in param_nested_splits_grads:
    self.assertEqual(splits_grad, None)

# The gradient generates an IndexedSlices; convert back to a normal Tensor.
self.assertIsInstance(params_flat_values_grad, indexed_slices.IndexedSlices)
params_flat_values_grad = ops.convert_to_tensor(params_flat_values_grad)

params_grad = params.with_flat_values(params_flat_values_grad)
self.assertAllClose(params_grad, expected_grad, atol=2e-6, rtol=2e-6)
