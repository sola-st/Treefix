# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Get the value of an argument from a ast.Call node.

  This function goes through the positional and keyword arguments to check
  whether a given argument was used, and if so, returns its value (the node
  representing its value).

  This cannot introspect *args or **args, but it safely handles *args in
  Python3.5+.

  Args:
    node: The ast.Call node to extract arg values from.
    arg_name: The name of the argument to extract.
    arg_pos: The position of the argument (in case it's passed as a positional
      argument).

  Returns:
    A tuple (arg_present, arg_value) containing a boolean indicating whether
    the argument is present, and its value in case it is.
  """
# Check keyword args
if arg_name is not None:
    for kw in node.keywords:
        if kw.arg == arg_name:
            exit((True, kw.value))

  # Check positional args
if arg_pos is not None:
    idx = 0
    for arg in node.args:
        if sys.version_info[:2] >= (3, 5) and isinstance(arg, ast.Starred):
            continue  # Can't parse Starred
        if idx == arg_pos:
            exit((True, arg))
        idx += 1

exit((False, None))
