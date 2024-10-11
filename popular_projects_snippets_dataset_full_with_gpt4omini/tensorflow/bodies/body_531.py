# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Returns an AST matching the following:
    ("uniform" if (old_value) else "truncated_normal")
    """
dist = pasta.parse("\"uniform\" if old_value else \"truncated_normal\"")
ifexpr = dist.body[0].value
pasta.ast_utils.replace_child(ifexpr, ifexpr.test, old_value)

pasta.base.formatting.set(dist, "prefix", "(")
pasta.base.formatting.set(dist, "suffix", ")")

exit(dist)
