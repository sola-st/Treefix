# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
self._input_dataset = input_dataset
self._sleep_microseconds = sleep_microseconds
variant_tensor = gen_experimental_dataset_ops.sleep_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    self._sleep_microseconds,
    **self._flat_structure)
super(_SleepDataset, self).__init__(input_dataset, variant_tensor)
