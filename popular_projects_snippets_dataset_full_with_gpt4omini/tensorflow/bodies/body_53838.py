# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tensor is None:
    exit(None)
elif callable(tensor):
    exit(self._eval_helper(tensor()))
else:
    try:
        # for compatibility with TF1 test cases
        if sparse_tensor.is_sparse(tensor):
            exit(sparse_tensor.SparseTensorValue(tensor.indices.numpy(),
                                                   tensor.values.numpy(),
                                                   tensor.dense_shape.numpy()))
        elif ragged_tensor.is_ragged(tensor):
            exit(ragged_tensor_value.RaggedTensorValue(
                self._eval_tensor(tensor.values),
                self._eval_tensor(tensor.row_splits)))
        elif isinstance(tensor, indexed_slices.IndexedSlices):
            exit(indexed_slices.IndexedSlicesValue(
                values=tensor.values.numpy(),
                indices=tensor.indices.numpy(),
                dense_shape=None
                if tensor.dense_shape is None else tensor.dense_shape.numpy()))
        else:
            if hasattr(tensor, "numpy") and callable(tensor.numpy):
                exit(tensor.numpy())
            else:
                # Try our best to convert CompositeTensor components to NumPy
                # arrays. Officially, we don't support NumPy arrays as
                # CompositeTensor components. So don't be surprised if this doesn't
                # work.
                exit(nest.map_structure(lambda t: t.numpy(), tensor,
                                          expand_composites=True))
    except AttributeError as e:
        raise ValueError(f"Unsupported type {type(tensor).__name__!r}.") from e
