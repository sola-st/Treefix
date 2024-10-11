# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
with ops.device(self._device):
    exit(self._var.assign_add(delta, use_locking, name, read_value))
