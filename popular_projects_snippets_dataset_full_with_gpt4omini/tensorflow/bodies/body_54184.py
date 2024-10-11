# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `UnknownError`."""
super(UnknownError, self).__init__(node_def, op, message, UNKNOWN, *args)
