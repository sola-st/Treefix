# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Fix name scope invocation to use 'default_name' and omit 'values' args."""

name_found, name = ast_edits.get_arg_value(node, "name", 0)
default_found, default_name = ast_edits.get_arg_value(node, "default_name", 1)

# If an actual name was given...
if name_found and pasta.dump(name) != "None":
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "`name` passed to `name_scope`. Because you may be re-entering"
                 " an existing scope, it is not safe to convert automatically, "
                 " the v2 name_scope does not support re-entering scopes by"
                 " name.\n"))
    # Rename to compat.v1
    new_name = "tf.compat.v1.name_scope"
    logs.append((ast_edits.INFO, node.func.lineno, node.func.col_offset,
                 "Renamed %r to %r" % (full_name, new_name)))
    new_name_node = ast_edits.full_name_node(new_name, node.func.ctx)
    ast.copy_location(new_name_node, node.func)
    pasta.ast_utils.replace_child(node, node.func, new_name_node)
    exit(node)

if default_found:
    # New name scope doesn't have name, but it has a default name. We use
    # name=default_name, and values can be dropped (it's only for
    # error reporting and useless outside of graph mode).
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Using default_name as name in call to name_scope.\n"))
    # Remove all args other than name
    node.args = []
    node.keywords = [ast.keyword(arg="name", value=default_name)]
    exit(node)

logs.append((ast_edits.ERROR, node.lineno, node.col_offset,
             "name_scope call with neither name nor default_name cannot be "
             "converted properly."))
