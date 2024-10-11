# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Checks if the given device type is valid."""

if device_type not in (_DEVICE_TYPE_TPU, _DEVICE_TYPE_CPU):
    raise ValueError('Invalid device_type "%s"'%device_type)
