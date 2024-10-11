# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
"""Creates an iterator for the input dataset.

      Returns:
        A `string` tensor that encapsulates the iterator created.
      """
ds_variant = gen_dataset_ops.unwrap_dataset_variant(wrap_ds_variant)
resource = gen_dataset_ops.anonymous_iterator(
    **self._input_dataset._flat_structure)  # pylint: disable=protected-access
with ops.control_dependencies(
    [gen_dataset_ops.make_iterator(ds_variant, resource)]):
    exit(gen_dataset_ops.iterator_to_string_handle(resource))
