# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Updates references to contrib.layers.variance_scaling_initializer.

  Transforms:
  tf.contrib.layers.variance_scaling_initializer(
    factor, mode, uniform, seed, dtype
  ) to
  tf.compat.v1.keras.initializers.VarianceScaling(
      scale=factor, mode=mode.lower(),
      distribution=("uniform" if uniform else "truncated_normal"),
      seed=seed, dtype=dtype)

  And handles the case where no factor is provided and scale needs to be
  set to 2.0 to match contrib's default instead of tf.keras.initializer's
  default of 1.0
  """
def _replace_distribution(parent, old_value):
    """Replaces old_value: ("uniform" if (old_value) else "truncated_normal")"""
    new_value = pasta.parse(
        "\"uniform\" if old_value else \"truncated_normal\"")
    ifexpr = new_value.body[0].value
    pasta.ast_utils.replace_child(ifexpr, ifexpr.test, old_value)

    pasta.ast_utils.replace_child(parent, old_value, new_value)

    pasta.base.formatting.set(new_value, "prefix", "(")
    pasta.base.formatting.set(new_value, "suffix", ")")

def _replace_mode(parent, old_value):
    """Replaces old_value with (old_value).lower()."""
    new_value = pasta.parse("mode.lower()")
    mode = new_value.body[0].value.func
    pasta.ast_utils.replace_child(mode, mode.value, old_value)

    # This copies the prefix and suffix on old_value to new_value.
    pasta.ast_utils.replace_child(parent, old_value, new_value)

    # Put parentheses around keep_prob.value (and remove the old prefix/
    # suffix, they should only be around new_value).
    pasta.base.formatting.set(old_value, "prefix", "(")
    pasta.base.formatting.set(old_value, "suffix", ")")

# Need to keep track of scale because slim & keras
# have different defaults
found_scale = False
for keyword_arg in node.keywords:
    if keyword_arg.arg == "factor":
        keyword_arg.arg = "scale"
        found_scale = True
    if keyword_arg.arg == "mode":
        _replace_mode(keyword_arg, keyword_arg.value)
    if keyword_arg.arg == "uniform":
        keyword_arg.arg = "distribution"
        _replace_distribution(keyword_arg, keyword_arg.value)

  # Handle any detected positional arguments
if len(node.args) >= 1:
    found_scale = True
if len(node.args) >= 2:
    _replace_mode(node, node.args[1])
if len(node.args) >= 3:
    _replace_distribution(node, node.args[2])

# If no scale was provided, make tf 2.0 use slim's default factor
if not found_scale:
    # Parse with pasta instead of ast to avoid emitting a spurious trailing \n.
    scale_value = pasta.parse("2.0")
    node.keywords = ([ast.keyword(arg="scale", value=scale_value)]
                     + node.keywords)

lineno = node.func.value.lineno
col_offset = node.func.value.col_offset
node.func.value = ast_edits.full_name_node("tf.compat.v1.keras.initializers")
node.func.value.lineno = lineno
node.func.value.col_offset = col_offset
node.func.attr = "VarianceScaling"

logs.append((ast_edits.INFO, node.lineno, node.col_offset,
             "Changing tf.contrib.layers.variance_scaling_initializer"
             " to a tf.compat.v1.keras.initializers.VarianceScaling and"
             " converting arguments.\n"))

exit(node)
