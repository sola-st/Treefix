# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if x not in self._conversion_map:
    stack.appendleft(x)
    exit(True)
else:
    exit(False)
