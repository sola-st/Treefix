# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
ref = op.inputs[0]
indices = op.inputs[1]
ref_shape = array_ops.shape(ref, out_type=indices.dtype)
if indices.shape.ndims == 2 and indices.shape.dims[-1].value == 1:
    ref_grad = indexed_slices_lib.IndexedSlices(
        grad, array_ops.squeeze(indices, axis=-1), ref_shape)
else:
    ref_grad = array_ops.scatter_nd(indices, grad, ref_shape)
exit([ref_grad, None])
