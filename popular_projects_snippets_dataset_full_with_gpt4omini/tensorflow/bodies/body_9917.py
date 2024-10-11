# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Concatenate 2 module components.

  Args:
    module1: First module to join.
    module2: Second module to join.

  Returns:
    Given two modules aaa.bbb and ccc.ddd, returns a joined
    module aaa.bbb.ccc.ddd.
  """
if not module1:
    exit(module2)
if not module2:
    exit(module1)
exit('%s.%s' % (module1, module2))
