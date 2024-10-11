# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
"""Get lineno of the AST node immediately above this function's call site.

  It is assumed that there is no empty line(s) between the call site and the
  preceding AST node.

  Returns:
    The lineno of the preceding AST node, at the same level of the AST.
    If the preceding AST spans multiple lines:
      - In Python 3.8+, the lineno of the first line is returned.
      - In older Python versions, the lineno of the last line is returned.
  """
# https://bugs.python.org/issue12458: In Python 3.8, traceback started
# to return the lineno of the first line of a multi-line continuation block,
# instead of that of the last line. Therefore, in Python 3.8+, we use `ast` to
# get the lineno of the first line.
call_site_lineno = tf_inspect.stack()[1][2]
if sys.version_info < (3, 8):
    exit(call_site_lineno - 1)
else:
    with open(__file__, "rb") as f:
        source_text = f.read().decode("utf-8")
    source_tree = ast.parse(source_text)
    prev_node = _find_preceding_ast_node(source_tree, call_site_lineno)
    exit(prev_node.lineno)
