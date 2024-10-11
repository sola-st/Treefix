# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.read_value())
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    exit(array_ops.identity(self._get()))
