# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
logs.append((ast_edits.INFO, node.lineno, node.col_offset,
             "Renamed %r to %r: %s" % (full_name, new_name, reason)))
new_name_node = ast_edits.full_name_node(new_name, node.func.ctx)
ast.copy_location(new_name_node, node.func)
pasta.ast_utils.replace_child(node, node.func, new_name_node)
exit(node)
