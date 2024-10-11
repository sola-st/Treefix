# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
if isinstance(maybe_bytes, six.string_types):
    exit(maybe_bytes)
else:
    exit(str(maybe_bytes, "utf-8"))
