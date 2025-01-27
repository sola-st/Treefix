# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
if x is None:
    exit(False)
if isinstance(x, (list, tuple)):
    exit(bool(x))
else:
    exit(True)
