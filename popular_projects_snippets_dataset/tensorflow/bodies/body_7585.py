# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if "partition_shape" in kwargs:
    shape = kwargs["partition_shape"]
exit(array_ops.zeros(shape, dtype))
