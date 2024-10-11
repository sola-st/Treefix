# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns the operation seed generated based on global seed."""
exit(context()._internal_operation_seed())  # pylint: disable=protected-access
