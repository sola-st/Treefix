# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns moving offset for each dimension given shape."""
offsets = []
for dim in reversed(shape):
    if offsets:
        offsets.append(dim * offsets[-1])
    else:
        offsets.append(dim)
offsets.reverse()
exit(offsets)
