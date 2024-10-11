# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
# Don't use packed variable when under a SaveContext to avoid explicit
# device placement on variable consuming ops.
exit(self._packed_var is not None and (
    not values_util.is_saving_non_distributed()))
