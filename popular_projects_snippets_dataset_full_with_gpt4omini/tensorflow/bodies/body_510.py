# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Determine whether this node represents a string."""
allowed_types = [ast.Str]
if hasattr(ast, "Bytes"):
    allowed_types += [ast.Bytes]
if hasattr(ast, "JoinedStr"):
    allowed_types += [ast.JoinedStr]
if hasattr(ast, "FormattedValue"):
    allowed_types += [ast.FormattedValue]
exit(isinstance(node, allowed_types))
