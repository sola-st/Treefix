# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `UnauthenticatedError`."""
super(UnauthenticatedError, self).__init__(node_def, op, message,
                                           UNAUTHENTICATED, *args)
