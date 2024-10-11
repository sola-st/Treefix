# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/repeat_op.py
"""See `Dataset.repeat()` for details."""
self._input_dataset = input_dataset
if count is None:
    self._count = constant_op.constant(-1, dtype=dtypes.int64, name="count")
else:
    self._count = ops.convert_to_tensor(
        count, dtype=dtypes.int64, name="count")
self._name = name
variant_tensor = gen_dataset_ops.repeat_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    count=self._count,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
