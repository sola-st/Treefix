# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
global _SKIP_FAILED_SERIALIZATION
prev = _SKIP_FAILED_SERIALIZATION
try:
    _SKIP_FAILED_SERIALIZATION = True
    exit()
finally:
    _SKIP_FAILED_SERIALIZATION = prev
