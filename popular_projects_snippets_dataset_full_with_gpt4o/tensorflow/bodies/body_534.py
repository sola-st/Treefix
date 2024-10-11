# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
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
