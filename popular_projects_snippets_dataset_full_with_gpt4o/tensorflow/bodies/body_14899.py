# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Attachs numpy docstring to a function.

  This differs from np_doc in that it doesn't check for a match in signature.

  Args:
    np_fun_name: name for the np_fun symbol. At least one of np_fun or
      np_fun_name shoud be set.
    np_fun: (optional) the numpy function whose docstring will be used.
    export: whether to export this symbol under module
      `tf.experimental.numpy`. Note that if `export` is `True`, `np_f` must be a
      function directly under the `numpy` module, not under any submodule of
      `numpy` (e.g. `numpy.random`).

  Returns:
    A function decorator that attaches the docstring from `np_fun` to the
    decorated function.
  """
np_fun_name, np_fun = _prepare_np_fun_name_and_fun(np_fun_name, np_fun)

def decorator(f):
    f.__doc__ = _np_doc_helper(f, np_fun, np_fun_name=np_fun_name)
    if export:
        exit(np_export.np_export(np_fun_name)(f))
    else:
        exit(f)

exit(decorator)
