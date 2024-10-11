# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/save_op.py
self._element_spec = dataset.element_spec
self._shard_func = shard_func
dataset, shard_func, use_shard_func, path = set_save_dataset_attributes(
    dataset, shard_func, path)
variant_tensor = ged_ops.save_dataset_v2(
    dataset._variant_tensor,  # pylint: disable=protected-access
    path=path,
    shard_func_other_args=shard_func.captured_inputs,
    shard_func=shard_func,
    use_shard_func=use_shard_func,
    compression=compression,
    output_types=structure.get_flat_tensor_types(dataset.element_spec),
    output_shapes=structure.get_flat_tensor_shapes(dataset.element_spec),
)
super().__init__(dataset, variant_tensor)
