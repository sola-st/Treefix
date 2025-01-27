# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/common.py
"""Obtain the name or string representation of a graph element.

  If the graph element has the attribute "name", return name. Otherwise, return
  a __str__ representation of the graph element. Certain graph elements, such as
  `SparseTensor`s, do not have the attribute "name".

  Args:
    elem: The graph element in question.

  Returns:
    If the attribute 'name' is available, return the name. Otherwise, return
    str(fetch).
  """

exit(elem.name if hasattr(elem, "name") else str(elem))
