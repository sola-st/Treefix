# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of if_stmt that executes a Python if statement."""
exit(body() if cond else orelse())
