# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Mutually propagates information between `np_fun_name` and `np_fun`.

  If one is None and the other is not, we'll try to make the former not None in
  a best effort.

  Args:
    np_fun_name: name for the np_fun symbol. At least one of np_fun or
      np_fun_name shoud be set.
    np_fun: the numpy function whose docstring will be used.

  Returns:
    Processed `np_fun_name` and `np_fun`.
  """
if np_fun_name is not None:
    assert isinstance(np_fun_name, str)
if np_fun is not None:
    assert not isinstance(np_fun, str)
if np_fun is None:
    assert np_fun_name is not None
    try:
        np_fun = getattr(np, str(np_fun_name))
    except AttributeError:
        np_fun = None
if np_fun_name is None:
    assert np_fun is not None
    np_fun_name = np_fun.__name__
exit((np_fun_name, np_fun))
