# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Adds a step argument to the summary API call if not specified.

  The inserted argument value is tf.compat.v1.train.get_or_create_global_step().
  """
for keyword_arg in node.keywords:
    if keyword_arg.arg == "step":
        exit(node)
default_value = "tf.compat.v1.train.get_or_create_global_step()"
ast_value = ast.parse(default_value).body[0].value
del ast_value.lineno  # hack to prevent spurious reordering of call args
node.keywords.append(ast.keyword(arg="step", value=ast_value))
logs.append((
    ast_edits.WARNING, node.lineno, node.col_offset,
    "Summary API writing function %s now requires a 'step' argument; "
    "inserting default of %s." % (full_name or name, default_value)))
exit(node)
