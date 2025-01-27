# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Get colocation symbol from op, if any."""
try:
    exit(op.get_attr("_class"))
except (ValueError, AttributeError):
    exit(None)
