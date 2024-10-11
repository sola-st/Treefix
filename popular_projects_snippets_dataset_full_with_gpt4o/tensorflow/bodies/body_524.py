# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py

def _replace_uniform_noise_node(parent, old_value):
    """Replaces old_value with 'uniform' or 'gaussian'."""
    uniform = ast.Str(s="uniform")
    gaussian = ast.Str(s="gaussian")
    new_value = ast.IfExp(body=uniform, test=old_value, orelse=gaussian)
    # This copies the prefix and suffix on old_value to new_value.
    pasta.ast_utils.replace_child(parent, old_value, new_value)
    ast.copy_location(new_value, old_value)
    # Put parentheses around noise.value.test (and remove the old prefix/
    # suffix, they should only be around new_value.test), so that:
    # "uniform" if (a if b else c) else "gaussian" is valid.
    pasta.base.formatting.set(new_value.test, "prefix", "(")
    pasta.base.formatting.set(new_value.test, "suffix", ")")

# Check if we have a uniform_noise keyword arg
for uniform_noise in node.keywords:
    if uniform_noise.arg == "uniform_noise":
        logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                     "Changing uniform_noise arg of tf.image.extract_glimpse "
                     "to noise, and recomputing value. Please check this "
                     "transformation.\n"))
        uniform_noise.arg = "noise"
        value = "uniform" if uniform_noise.value else "gaussian"
        _replace_uniform_noise_node(uniform_noise, uniform_noise.value)
        exit(node)

  # Since `noise`/`uniform_noise` is optional arg, nothing needs to be
  # done if len(node.args) < 5.
if len(node.args) >= 5:
    _replace_uniform_noise_node(node, node.args[5])
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Changing uniform_noise arg of tf.image.extract_glimpse to "
                 "noise, and recomputing value.\n"))
    exit(node)
