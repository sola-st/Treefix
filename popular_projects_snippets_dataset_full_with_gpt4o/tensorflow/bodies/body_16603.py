# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
if isinstance(t, int):
    exit(t)
else:
    y = 1
    for x in t:
        y *= x
    exit(y)
