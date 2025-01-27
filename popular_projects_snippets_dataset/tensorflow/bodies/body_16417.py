# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Converts Python padding to C++ padding for ops which take EXPLICIT padding.

  Args:
    padding: the `padding` argument for a Python op which supports EXPLICIT
      padding.
    expected_length: Expected number of entries in the padding list when
      explicit padding is used.

  Returns:
    (padding, explicit_paddings) pair, which should be passed as attributes to a
    C++ op.

  Raises:
    ValueError: If padding is invalid.
  """
explicit_paddings = []
if padding == "EXPLICIT":
    raise ValueError("'EXPLICIT' is not a valid value for `padding`. To use "
                     "explicit padding, `padding` must be a list.")
if isinstance(padding, (list, tuple)):
    for i, dim_paddings in enumerate(padding):
        if not isinstance(dim_paddings, (list, tuple)):
            raise ValueError("When `padding` is a list, each element of `padding` "
                             "must be a list/tuple of size 2. Received: "
                             f"padding={padding} with element at index {i} of type "
                             f"{type(dim_paddings)}")
        if len(dim_paddings) != 2:
            raise ValueError("When `padding` is a list, each element of `padding` "
                             "must be a list/tuple of size 2. Received: "
                             f"padding={padding} with element at index {i} of size "
                             f"{len(dim_paddings)}")
        explicit_paddings.extend(dim_paddings)
    if len(padding) != expected_length:
        raise ValueError(
            f"When padding is a list, it must be of size {expected_length}. "
            f"Received: padding={padding} of size {len(padding)}")
    padding = "EXPLICIT"
exit((padding, explicit_paddings))
