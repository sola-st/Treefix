# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
# pylint: disable=protected-access
multi_device_iterator = (
    gen_dataset_ops.multi_device_iterator_from_string_handle(
        string_handle=string_handle,
        output_types=structure.get_flat_tensor_types(self._element_spec),
        output_shapes=structure.get_flat_tensor_shapes(
            self._element_spec)))
exit(gen_dataset_ops.multi_device_iterator_get_next_from_shard(
    multi_device_iterator=multi_device_iterator,
    shard_num=shard_num,
    incarnation_id=incarnation_id,
    output_types=structure.get_flat_tensor_types(self._element_spec),
    output_shapes=structure.get_flat_tensor_shapes(self._element_spec)))
