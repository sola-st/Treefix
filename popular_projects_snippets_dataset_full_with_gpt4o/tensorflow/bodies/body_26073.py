# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/unbatch_op.py
"""See `unbatch()` for more details."""
flat_shapes = input_dataset._flat_shapes  # pylint: disable=protected-access
if any(s.ndims == 0 for s in flat_shapes):
    raise ValueError("Cannot unbatch an input with scalar components.")
known_batch_dim = tensor_shape.Dimension(None)
for s in flat_shapes:
    try:
        known_batch_dim = known_batch_dim.merge_with(s[0])
    except ValueError as e:
        raise ValueError(
            f"`unbatch()` is only supported for datasets of elements whose "
            f"components have a matching leading dimension. Encountered both "
            f"{known_batch_dim} and {s[0]}.") from e
self._input_dataset = input_dataset
self._structure = nest.map_structure(
    lambda component_spec: component_spec._unbatch(),  # pylint: disable=protected-access
    dataset_ops.get_structure(input_dataset))
self._name = name
variant_tensor = ged_ops.unbatch_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
