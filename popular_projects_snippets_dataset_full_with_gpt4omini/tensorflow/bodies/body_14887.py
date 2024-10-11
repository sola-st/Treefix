# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
r"""Selects the form of the original numpy docstrings.

  This function sets a global variable that controls how a tf-numpy symbol's
  docstring should refer to the original numpy docstring. If `value` is
  `'inlined'`, the numpy docstring will be verbatim copied into the tf-numpy
  docstring. Otherwise, a link to the original numpy docstring will be
  added. Which numpy version the link points to depends on `value`:
  * `'stable'`: the current stable version;
  * `'dev'`: the current development version;
  * pattern `\d+(\.\d+(\.\d+)?)?`: `value` will be treated as a version number,
    e.g. '1.16'.

  Args:
    value: the value to set the global variable to.
  """
global _np_doc_form
_np_doc_form = value
