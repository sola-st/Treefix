# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Creates a new Dimension with the given value."""
if isinstance(value, int):  # Most common case.
    if value < 0:
        raise ValueError("Dimension %d must be >= 0" % value)
    self._value = value
elif value is None:
    self._value = None
elif isinstance(value, Dimension):
    self._value = value._value
else:
    try:
        # int(...) compensates for the int/long dichotomy on Python 2.X.
        # TODO(b/143206389): Remove once we fully migrate to 3.X.
        self._value = int(value.__index__())
    except AttributeError:
        raise TypeError(
            "Dimension value must be integer or None or have "
            "an __index__ method, got value '{0!r}' with type '{1!r}'".format(
                value, type(value))) from None
    if self._value < 0:
        raise ValueError("Dimension %d must be >= 0" % self._value)
