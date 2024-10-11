# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns the eager mode seed."""
exit(context()._seed)  # pylint: disable=protected-access
