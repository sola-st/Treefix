# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Sets the eager mode seed."""
context()._set_global_seed(seed)  # pylint: disable=protected-access
