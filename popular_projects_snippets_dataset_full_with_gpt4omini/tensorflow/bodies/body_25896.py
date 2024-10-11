# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/batch_op.py
"""See `Dataset.batch()` for details."""
self._input_dataset = input_dataset
self._batch_size = ops.convert_to_tensor(
    batch_size, dtype=dtypes.int64, name="batch_size")
self._drop_remainder = ops.convert_to_tensor(
    drop_remainder, dtype=dtypes.bool, name="drop_remainder")

constant_drop_remainder = tensor_util.constant_value(self._drop_remainder)
# pylint: disable=protected-access
if constant_drop_remainder:
    # NOTE(mrry): `constant_drop_remainder` may be `None` (unknown statically)
    # or `False` (explicitly retaining the remainder).
    # pylint: disable=g-long-lambda
    constant_batch_size = tensor_util.constant_value(self._batch_size)
    self._structure = nest.map_structure(
        lambda component_spec: component_spec._batch(constant_batch_size),
        input_dataset.element_spec)
else:
    self._structure = nest.map_structure(
        lambda component_spec: component_spec._batch(None),
        input_dataset.element_spec)

self._name = name
variant_tensor = gen_dataset_ops.batch_dataset_v2(
    input_dataset._variant_tensor,
    batch_size=self._batch_size,
    drop_remainder=self._drop_remainder,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
