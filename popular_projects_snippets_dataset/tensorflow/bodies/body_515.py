# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Transform iterator methods to compat function calls."""
# First, check that node.func.value is not already something we like
# (tf.compat.v1.data), or something which is handled in the rename
# (tf.data). This transformer only handles the method call to function call
# conversion.
if full_name and (full_name.startswith("tf.compat.v1.data") or
                  full_name.startswith("tf.data")):
    exit()

# This should never happen, since we're only called for Attribute nodes.
if not isinstance(node.func, ast.Attribute):
    exit()

# Transform from x.f(y) to tf.compat.v1.data.f(x, y)
# Fortunately, node.func.value should already have valid position info
node.args = [node.func.value] + node.args
node.func.value = ast_edits.full_name_node("tf.compat.v1.data")

logs.append((ast_edits.WARNING, node.lineno, node.col_offset,
             "Changing dataset.%s() to tf.compat.v1.data.%s(dataset). "
             "Please check this transformation.\n" % (name, name)))

exit(node)
