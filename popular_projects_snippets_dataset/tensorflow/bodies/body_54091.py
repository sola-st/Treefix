# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Fetch colocation file, line, and nesting and return a summary string."""
# pylint: disable=protected-access
exit(_compute_colocation_summary_from_dict(op.name, op._colocation_dict,
                                             prefix))
