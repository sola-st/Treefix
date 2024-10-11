# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if context.executing_eagerly():
    exit()

rt = RaggedTensor.from_row_splits([1.0, 2.0], row_splits=[0, 2, 2])
v1 = rt._to_variant()
v2 = array_ops.stack([array_ops.stack([v1])])
y = RaggedTensor._from_variant(v2, rt.dtype, output_ragged_rank=3)

with self.assertRaisesRegex(
    ValueError, 'Unable to compute gradient: RaggedTensorToVariant '
    'can currently only generate 0D or 1D output.'):
    gradients_impl.gradients(ys=y.flat_values, xs=rt.flat_values)
