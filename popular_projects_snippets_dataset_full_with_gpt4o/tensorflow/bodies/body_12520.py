# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
if all(p == 1 for p in self._partitions):
    exit([0])
else:
    exit([i for i, p in enumerate(self._partitions) if p > 1])
