# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/prefetch_op.py
"""See `Dataset.prefetch()` for details."""
self._input_dataset = input_dataset
if buffer_size is None:
    buffer_size = dataset_ops.AUTOTUNE
self._buffer_size = ops.convert_to_tensor(
    buffer_size, dtype=dtypes.int64, name="buffer_size")
self._name = name
# pylint: disable=protected-access
# We colocate the prefetch dataset with its input as this collocation only
# happens automatically in graph mode.
with ops.colocate_with(input_dataset._variant_tensor):
    variant_tensor = gen_dataset_ops.prefetch_dataset(
        input_dataset._variant_tensor,
        buffer_size=self._buffer_size,
        slack_period=slack_period,
        **self._common_args)
super().__init__(input_dataset, variant_tensor)
