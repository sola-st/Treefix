# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
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
