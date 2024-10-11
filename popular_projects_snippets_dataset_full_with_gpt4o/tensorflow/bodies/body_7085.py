# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
with ops.device(self._device):
    exit(self._var.assign(value, use_locking, name, read_value))
