# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
"""Recursively imports all the sub-modules under a root package.

  Args:
    root: A python package.
  """
for _, name, _ in pkgutil.walk_packages(
    root.__path__, prefix=root.__name__ + '.'):
    try:
        importlib.import_module(name)
    except (AttributeError, ImportError):
        pass
