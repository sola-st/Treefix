# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
self._input_dataset = input_dataset

self._element_spec = input_dataset.element_spec
variant_tensor = ged_ops.auto_shard_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    num_workers=num_workers,
    index=index,
    auto_shard_policy=int(
        input_dataset.options().experimental_distribute.auto_shard_policy),
    num_replicas=num_replicas,
    **self._flat_structure)
super(_AutoShardDataset, self).__init__(input_dataset, variant_tensor)
