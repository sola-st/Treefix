# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ragged_batch_op.py
"""Constructs a new _DenseToRaggedDataset.

    Args:
      input_dataset: The dataset whose tf.Tensor elements should be made ragged.
      row_splits_dtype: The dtype that should be used for the `row_splits` of
        any new ragged tensors.  Existing `tf.RaggedTensor` elements do *not*
        have their row_splits dtype changed.
      name: (Optional.) A string indicating a name for the `tf.data` operation.
    """
# Replace each TensorSpec in the input dataset's structure with a
# corresponding RaggedTensorSpec.
def to_ragged_spec(spec):
    """Returns the new spec based on RaggedTensors."""
    if (not isinstance(spec, tensor_spec.TensorSpec) or
        spec.shape.rank is None or
        spec.shape.is_fully_defined()):
        exit(spec)
    else:
        ragged_rank = max([
            axis for (axis, size) in enumerate(spec.shape.as_list())
            if size is None
        ])
        exit(ragged_tensor.RaggedTensorSpec(
            shape=spec.shape,
            dtype=spec.dtype,
            ragged_rank=ragged_rank,
            row_splits_dtype=row_splits_dtype))

self._structure = nest.map_structure(to_ragged_spec,
                                     input_dataset.element_spec)

# Replace each tf.Tensor value in the input dataset with a variant-encoded
# RaggedTensor. Since we're updating the corresponding structure to be
# a RaggedTensorSpec, this variant-encoded tensor will be decoded with
# RaggedTensorSpec._from_tensor_list.
def to_ragged_variant(value):
    """Re-encode Tensors as RaggedTensors."""
    if (not isinstance(value, ops.Tensor) or
        value.shape.rank is None or
        value.shape.is_fully_defined()):
        exit(value)
    else:
        spec = to_ragged_spec(tensor_spec.TensorSpec.from_tensor(value))
        if spec._ragged_rank > 0:  # pylint: disable=protected-access
            value = ragged_tensor.RaggedTensor.from_tensor(
                value, ragged_rank=spec._ragged_rank)  # pylint: disable=protected-access
        exit(spec._to_tensor_list(value)[0])  # pylint: disable=protected-access

    # Tuples are automatically unpacked by `dataset.map` so we repack them.
if structured_function._should_unpack(input_dataset.element_spec):  # pylint: disable=protected-access
    map_fn = lambda *value: nest.map_structure(to_ragged_variant, value)
else:
    map_fn = lambda value: nest.map_structure(to_ragged_variant, value)

self._mapped_dataset = input_dataset.map(map_fn)
self._name = name
variant = self._mapped_dataset._variant_tensor  # pylint: disable=protected-access
super().__init__(input_dataset, variant)
