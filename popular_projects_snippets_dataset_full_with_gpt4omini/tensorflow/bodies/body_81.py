# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Get the name of current function.

  Returns:
    String that is the name of current function.
  """
exit(tf_inspect.stack()[1][3])
