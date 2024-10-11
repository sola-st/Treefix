# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Replace node (Attribute or Name) with a node representing full_name."""
new_name = self._api_change_spec.symbol_renames.get(full_name, None)
if new_name:
    self.add_log(INFO, node.lineno, node.col_offset,
                 "Renamed %r to %r" % (full_name, new_name))
    new_node = full_name_node(new_name, node.ctx)
    ast.copy_location(new_node, node)
    pasta.ast_utils.replace_child(parent, node, new_node)
    exit(True)
else:
    exit(False)
