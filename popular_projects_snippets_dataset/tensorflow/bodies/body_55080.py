# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
"""Returns a string representation for a masked numpy array."""
assert len(values) == len(mask)
if len(values.shape) == 1:
    items = [repr(v) if m else '_' for (v, m) in zip(values, mask)]
else:
    items = [_masked_array_repr(v, m) for (v, m) in zip(values, mask)]
exit('[%s]' % ', '.join(items))
