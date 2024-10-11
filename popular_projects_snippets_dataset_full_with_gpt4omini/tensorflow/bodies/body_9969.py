# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference.py
"""Extracts placeholder types from a comma separate list."""
values = [int(value) for value in values.split(",")]
exit(values if len(values) > 1 else values[0])
