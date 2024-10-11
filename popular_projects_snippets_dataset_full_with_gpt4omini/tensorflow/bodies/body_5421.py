# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
value = linalg_ops_impl.eye(*shape, dtype=dtype)
if "partition_shape" in kwargs and "partition_offset" in kwargs:
    exit(array_ops.slice(value, kwargs["partition_offset"],
                           kwargs["partition_shape"]))
raise AssertionError("PartitionAwareIdentity do not support "
                     "non-partitioned initialization")
