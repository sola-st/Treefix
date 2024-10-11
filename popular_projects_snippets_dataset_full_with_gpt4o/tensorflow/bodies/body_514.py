# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Adds an argument (as a final kwarg arg_name=arg_value_ast)."""
node.keywords.append(ast.keyword(arg=arg_name, value=arg_value_ast))
logs.append((
    ast_edits.INFO, node.lineno, node.col_offset,
    "Adding argument '%s' to call to %s." % (pasta.dump(node.keywords[-1]),
                                             full_name or name)
))
exit(node)
