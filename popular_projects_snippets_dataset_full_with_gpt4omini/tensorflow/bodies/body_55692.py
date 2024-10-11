# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
"""Return a copy of an existing stack frame with a new filename."""
frame = tb[idx]
exit(FrameSummary(
    filename,
    frame.lineno,
    frame.name,
    frame.line))
