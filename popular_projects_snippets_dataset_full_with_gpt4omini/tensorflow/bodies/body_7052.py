# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
for i, d in enumerate(self._devices):
    if d == device:
        exit(self._distributed_variables[i])
raise ValueError("Device %s is not found" % device)
