# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `InternalError`."""
super(InternalError, self).__init__(node_def, op, message, INTERNAL, *args)
