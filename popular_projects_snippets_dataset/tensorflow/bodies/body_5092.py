# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if not self._use_merge_call():
    exit(self._collective_ops)

if self._collective_ops_in_use:
    if isinstance(value, values.DistributedValues):
        value_int32 = True in {
            dtypes.as_dtype(v.dtype) == dtypes.int32 for v in value.values
        }
    else:
        value_int32 = dtypes.as_dtype(value.dtype) == dtypes.int32
    if value_int32:
        exit(cross_device_ops_lib.ReductionToOneDevice())
    else:
        exit(self._collective_ops)

exit(self._cross_device_ops or self._inferred_cross_device_ops)
