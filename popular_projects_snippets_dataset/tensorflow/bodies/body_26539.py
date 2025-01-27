# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""Destroys the iterator resource created.

      Args:
        string_handle: An iterator string handle created by _init_func
      Returns:
        Tensor constant 0
      """
iterator_resource = gen_dataset_ops.iterator_from_string_handle_v2(
    string_handle,
    **self._input_dataset._flat_structure)  # pylint: disable=protected-access
with ops.control_dependencies([
    resource_variable_ops.destroy_resource_op(
        iterator_resource, ignore_lookup_error=True)]):
    exit(array_ops.constant(0, dtypes.int64))
