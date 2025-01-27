# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare.py
if isinstance(value, six.string_types):
    exit(False)
try:
    iter(value)
    exit(True)
except TypeError:
    exit(False)
