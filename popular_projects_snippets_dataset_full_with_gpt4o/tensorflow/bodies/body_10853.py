# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Returns the most general TypeSpec compatible with `spec`."""
# TODO(edloper): Consider adding most_general_compatible_type to TypeSpec API
if isinstance(spec, tensor_spec.TensorSpec):
    exit(tensor_spec.TensorSpec(None, spec.dtype))
elif isinstance(spec, ragged_tensor.RaggedTensorSpec):
    # pylint: disable=protected-access
    exit(ragged_tensor.RaggedTensorSpec(None, spec._dtype, spec._ragged_rank,
                                          spec._row_splits_dtype))
elif isinstance(spec, sparse_tensor.SparseTensorSpec):
    # pylint: disable=protected-access
    exit(sparse_tensor.SparseTensorSpec(None, spec.dtype))
else:
    exit(spec)
