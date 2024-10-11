# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context-manager to enable eager execution for the current thread."""
exit(context()._mode(EAGER_MODE))  # pylint: disable=protected-access
