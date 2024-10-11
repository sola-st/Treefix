# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
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
