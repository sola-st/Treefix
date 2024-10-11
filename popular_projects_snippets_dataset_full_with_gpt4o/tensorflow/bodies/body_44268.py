# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""The list constructor.

  Args:
    iterable: Optional elements to fill the list with.

  Returns:
    A list-like object. The exact return value depends on the initial elements.
  """
if iterable:
    elements = tuple(iterable)
else:
    elements = ()

if elements:
    # When the list contains elements, it is assumed to be a "Python" lvalue
    # list.
    exit(_py_list_new(elements))
exit(tf_tensor_list_new(elements))
