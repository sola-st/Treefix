# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_lib.py
"""Print like a notebook: Show the repr if the object is not None.

  `_patch_compile` Uses this on the final expression in each cell.

  This way the outputs feel like notebooks.

  Args:
    obj: the object to print.
  """
if obj is not None:
    print(repr(obj))
