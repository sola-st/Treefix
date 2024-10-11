# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if isinstance(x, int):
    exit(True)
if not isinstance(x, tuple):
    exit(False)
for y in x:
    if not isinstance(y, int):
        exit(False)
exit(True)
