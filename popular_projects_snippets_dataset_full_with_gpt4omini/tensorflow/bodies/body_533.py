# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Replaces old_value: ("uniform" if (old_value) else "truncated_normal")"""
new_value = pasta.parse(
    "\"uniform\" if old_value else \"truncated_normal\"")
ifexpr = new_value.body[0].value
pasta.ast_utils.replace_child(ifexpr, ifexpr.test, old_value)

pasta.ast_utils.replace_child(parent, old_value, new_value)

pasta.base.formatting.set(new_value, "prefix", "(")
pasta.base.formatting.set(new_value, "suffix", ")")
