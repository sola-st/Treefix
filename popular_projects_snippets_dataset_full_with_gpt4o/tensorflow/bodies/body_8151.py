# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
if self._cached_value is not None:
    with ops.control_dependencies([self._cached_value]):
        exit()
else:
    exit()
