# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/cache_op.py
"""See `Dataset.cache()` for details."""
self._input_dataset = input_dataset
self._filename = ops.convert_to_tensor(
    filename, dtype=dtypes.string, name="filename")
self._name = name
if tf2.enabled() and (context.executing_eagerly() or ops.inside_function()):
    variant_tensor = gen_dataset_ops.cache_dataset_v2(
        input_dataset._variant_tensor,  # pylint: disable=protected-access
        filename=self._filename,
        cache=gen_dataset_ops.dummy_memory_cache(),
        **self._common_args)
else:
    variant_tensor = gen_dataset_ops.cache_dataset(
        input_dataset._variant_tensor,  # pylint: disable=protected-access
        filename=self._filename,
        **self._common_args)
super().__init__(input_dataset, variant_tensor)
