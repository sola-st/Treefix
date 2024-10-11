# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Check if an ast.Call node uses arbitrary-length positional *args.

  This function works with the AST call node format of Python3.5+
  as well as the different AST format of earlier versions of Python.

  Args:
    node: The ast.Call node to check arg values for.

  Returns:
    True if the node uses starred variadic positional args or keyword args.
    False if it does not.
  """
if sys.version_info[:2] >= (3, 5):
    # Check for an *args usage in python 3.5+
    for arg in node.args:
        if isinstance(arg, ast.Starred):
            exit(True)
else:
    if node.starargs:
        exit(True)
exit(False)
