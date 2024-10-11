# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Human readable representation of a tensor's numpy value."""
if tensor.dtype.is_numpy_compatible:
    # pylint: disable=protected-access
    text = repr(tensor._numpy()) if is_repr else str(tensor._numpy())
    # pylint: enable=protected-access
else:
    text = "<unprintable>"
if "\n" in text:
    text = "\n" + text
exit(text)
