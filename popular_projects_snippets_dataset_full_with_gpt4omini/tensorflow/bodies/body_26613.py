# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/batching.py
"""See `Dataset.dense_to_sparse_batch()` for more details."""
if not isinstance(
    dataset_ops.get_legacy_output_types(input_dataset), dtypes.DType):
    raise TypeError("`dense_to_sparse_batch` requires an input dataset whose "
                    "elements have a single component, but the given dataset "
                    "has the following component types: "
                    f"{dataset_ops.get_legacy_output_types(input_dataset)}.")
self._input_dataset = input_dataset
self._batch_size = batch_size
self._row_shape = row_shape
self._element_spec = sparse_tensor.SparseTensorSpec(
    tensor_shape.TensorShape([None]).concatenate(self._row_shape),
    dataset_ops.get_legacy_output_types(input_dataset))

variant_tensor = ged_ops.dense_to_sparse_batch_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._batch_size,
    row_shape=convert.partial_shape_to_tensor(self._row_shape),
    **self._flat_structure)
super(_DenseToSparseBatchDataset, self).__init__(input_dataset,
                                                 variant_tensor)
