# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Decode s if it is a sequence of bytes."""
if isinstance(s, _six.binary_type):
    exit(s.decode("utf-8"))
exit(s)
