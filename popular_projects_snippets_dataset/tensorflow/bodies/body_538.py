# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Replace slim l2 regularizer with Keras one, with l=0.5*scale.

  Also drops the scope argument.
  """
def _replace_scale_node(parent, old_value):
    """Replaces old_value with 0.5*(old_value)."""
    half = ast.Num(n=0.5)
    half.lineno = 0
    half.col_offset = 0
    new_value = ast.BinOp(left=half, op=ast.Mult(),
                          right=old_value)
    # This copies the prefix and suffix on old_value to new_value.
    pasta.ast_utils.replace_child(parent, old_value, new_value)

    # Put parentheses around scale.value (and remove the old prefix/
    # suffix, they should only be around new_value).
    pasta.base.formatting.set(old_value, "prefix", "(")
    pasta.base.formatting.set(old_value, "suffix", ")")

# Check if we have a scale or scope keyword arg
scope_keyword = None
for keyword in node.keywords:
    if keyword.arg == "scale":
        keyword.arg = "l"
        _replace_scale_node(keyword, keyword.value)
    if keyword.arg == "scope":
        scope_keyword = keyword

  # Maybe it was a positional arg
if len(node.args) >= 1:
    _replace_scale_node(node, node.args[0])

# Remove the scope keyword or arg if it is present
if scope_keyword:
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Dropping scope arg from tf.contrib.layers.l2_regularizer,"
                 " because it is unsupported in tf.keras.regularizers.l2\n"))
    node.keywords.remove(scope_keyword)
if len(node.args) > 1:
    node.args = node.args[:1]
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Dropping scope arg from tf.contrib.layers.l2_regularizer,"
                 " because it is unsupported in tf.keras.regularizers.l2\n"))

logs.append((ast_edits.INFO, node.lineno, node.col_offset,
             "Multiplying scale arg of tf.contrib.layers.l2_regularizer"
             " by half to what tf.keras.regularizers.l2 expects.\n"))

lineno = node.func.value.lineno
col_offset = node.func.value.col_offset
node.func.value = ast_edits.full_name_node("tf.keras.regularizers")
node.func.value.lineno = lineno
node.func.value.col_offset = col_offset
node.func.attr = "l2"

exit(node)
