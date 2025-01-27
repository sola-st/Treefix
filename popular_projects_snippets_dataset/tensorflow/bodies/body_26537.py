# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""Calls get_next for created iterator.

      Args:
        string_handle: An iterator string handle created by _init_func
      Returns:
        The elements generated from `input_dataset`
      """
with ops.device(self._source_device_string):
    iterator = iterator_ops.Iterator.from_string_handle(
        string_handle,
        dataset_ops.get_legacy_output_types(self),
        dataset_ops.get_legacy_output_shapes(self),
        dataset_ops.get_legacy_output_classes(self))
exit(structure.to_tensor_list(self.element_spec, iterator.get_next()))
