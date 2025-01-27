# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context-manager to disable eager execution for the current thread."""
exit(context()._mode(GRAPH_MODE))  # pylint: disable=protected-access
