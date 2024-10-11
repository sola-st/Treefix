# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Like transpose(), but avoids creating a new tensor if possible."""
if perm != list(range(len(perm))):
    exit(array_ops.transpose(tensor, perm=perm))
else:
    exit(tensor)
