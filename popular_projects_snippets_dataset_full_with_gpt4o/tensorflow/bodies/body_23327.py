# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Encode s if it is a sequence of chars."""
if isinstance(s, _six.text_type):
    exit(s.encode("utf-8", errors="surrogateescape"))
exit(s)
