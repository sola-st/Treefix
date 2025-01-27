# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Replace keep_prob with 1-rate."""
def _replace_keep_prob_node(parent, old_value):
    """Replaces old_value with 1-(old_value)."""
    one = ast.Num(n=1)
    one.lineno = 0
    one.col_offset = 0
    new_value = ast.BinOp(left=one, op=ast.Sub(),
                          right=old_value)
    # This copies the prefix and suffix on old_value to new_value.
    pasta.ast_utils.replace_child(parent, old_value, new_value)
    ast.copy_location(new_value, old_value)
    # Put parentheses around keep_prob.value (and remove the old prefix/
    # suffix, they should only be around new_value).
    pasta.base.formatting.set(old_value, "prefix", "(")
    pasta.base.formatting.set(old_value, "suffix", ")")

# Check if we have a keep_prob keyword arg
for keep_prob in node.keywords:
    if keep_prob.arg == "keep_prob":
        logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                     "Changing keep_prob arg of tf.nn.dropout to rate\n"))
        keep_prob.arg = "rate"
        _replace_keep_prob_node(keep_prob, keep_prob.value)
        exit(node)

  # Maybe it was a positional arg
if len(node.args) < 2:
    logs.append((ast_edits.ERROR, node.lineno, node.col_offset,
                 "tf.nn.dropout called without arguments, so "
                 "automatic fix was disabled. tf.nn.dropout has changed "
                 "the semantics of the second argument."))
else:
    rate_arg = ast.keyword(arg="rate", value=node.args[1])
    _replace_keep_prob_node(rate_arg, rate_arg.value)
    node.keywords.append(rate_arg)
    del node.args[1]
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Changing keep_prob arg of tf.nn.dropout to rate, and "
                 "recomputing value.\n"))

    exit(node)
