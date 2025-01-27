# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Converts a variable to a tensor."""
if values_util.is_saving_non_distributed():
    exit(ops.convert_to_tensor(
        self._primary, dtype=dtype, name=name, as_ref=as_ref))
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    exit(ops.convert_to_tensor(
        self._get(), dtype=dtype, name=name, as_ref=as_ref))
