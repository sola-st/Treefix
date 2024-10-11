# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
if device_type == _DEVICE_TYPE_TPU:
    # pylint: disable=protected-access
    exit(tpu._TPU_REPLICATE_ATTR not in op.node_def.attr)
    # pylint: enable=protected-access
exit(False)
