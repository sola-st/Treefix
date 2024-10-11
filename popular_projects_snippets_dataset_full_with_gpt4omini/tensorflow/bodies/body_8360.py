# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
if control_input is not None and not self._use_ordering_token():
    exit(ops.control_dependencies([control_input]))
exit(ops.NullContextmanager())
