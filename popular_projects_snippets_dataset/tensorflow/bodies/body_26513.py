# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/shuffle_ops.py
self._input_dataset = input_dataset
self._buffer_size = ops.convert_to_tensor(
    buffer_size, dtype=dtypes.int64, name="buffer_size")
if count is None:
    self._count = constant_op.constant(-1, dtype=dtypes.int64, name="count")
else:
    self._count = ops.convert_to_tensor(
        count, dtype=dtypes.int64, name="count")
self._seed, self._seed2 = random_seed.get_seed(seed)
variant_tensor = gen_dataset_ops.shuffle_and_repeat_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    buffer_size=self._buffer_size,
    count=self._count,
    seed=self._seed,
    seed2=self._seed2,
    **self._flat_structure)
super(_ShuffleAndRepeatDataset, self).__init__(input_dataset,
                                               variant_tensor)
