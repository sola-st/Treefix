# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
# Lazy read is not supported.
with ops.control_dependencies([op]):
    exit(self.read_value())
