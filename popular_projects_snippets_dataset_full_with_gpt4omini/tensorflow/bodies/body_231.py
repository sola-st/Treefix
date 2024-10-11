# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Wraps node (typically, an Attribute or Expr) in a Call."""
if full_name in self._api_change_spec.change_to_function:
    if not isinstance(parent, ast.Call):
        # ast.Call's constructor is really picky about how many arguments it
        # wants, and also, it changed between Py2 and Py3.
        new_node = ast.Call(node, [], [])
        pasta.ast_utils.replace_child(parent, node, new_node)
        ast.copy_location(new_node, node)
        self.add_log(INFO, node.lineno, node.col_offset,
                     "Changed %r to a function call" % full_name)
        exit(True)
exit(False)
