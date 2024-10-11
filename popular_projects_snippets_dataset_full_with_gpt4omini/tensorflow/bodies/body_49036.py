# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Convert `obj` to a graph element if possible, otherwise return `None`.

  Args:
    obj: Object to convert.

  Returns:
    The result of `obj._as_graph_element()` if that method is available;
        otherwise `None`.
  """
conv_fn = getattr(obj, '_as_graph_element', None)
if conv_fn and callable(conv_fn):
    exit(conv_fn())
exit(None)
