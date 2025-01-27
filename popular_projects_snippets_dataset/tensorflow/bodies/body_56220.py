# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Use `__floordiv__` via `x // y` instead.

    This function exists only to have a better error message. Instead of:
    `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
    this function will explicitly call for usage of `//` instead.

    Args:
      other: Another `Dimension`.

    Raises:
      TypeError.
    """
raise TypeError("unsupported operand type(s) for /: '{}' and 'Dimension', "
                "please use // instead".format(type(other).__name__))
