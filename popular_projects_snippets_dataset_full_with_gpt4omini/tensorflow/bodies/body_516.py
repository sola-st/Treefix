# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
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
