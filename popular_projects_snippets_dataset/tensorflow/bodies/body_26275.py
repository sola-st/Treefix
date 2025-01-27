# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/rebatch_op.py
"""See `Dataset.rebatch` for details."""
self._input_dataset = input_dataset
self._batch_sizes = ops.convert_to_tensor(
    batch_sizes, dtype=dtypes.int64, name="batch_sizes")
self._drop_remainder = ops.convert_to_tensor(
    drop_remainder, dtype=dtypes.bool, name="drop_remainder")
self._name = name
new_batch_dim = self._compute_static_batch_dim()

# pylint: disable=protected-access
self._element_spec = nest.map_structure(
    lambda ts: ts._unbatch()._batch(new_batch_dim),
    dataset_ops.get_structure(input_dataset))
# pylint: enable=protected-access

# auto_shard rewrite assumes that there's normalize_to_dense before
# rebatch_dataset.
# LINT.IfChange
input_dataset = dataset_ops.normalize_to_dense(input_dataset)
variant_tensor = ged_ops.rebatch_dataset_v2(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    batch_sizes=batch_sizes,
    drop_remainder=drop_remainder,
    **self._flat_structure)
# LINT.ThenChange(//tensorflow/core/grappler/optimizers/data/auto_shard.cc)
super().__init__(input_dataset, variant_tensor)
