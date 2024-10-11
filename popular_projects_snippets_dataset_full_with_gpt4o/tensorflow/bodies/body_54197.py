# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `UnavailableError`."""
super(UnavailableError, self).__init__(node_def, op, message, UNAVAILABLE,
                                       *args)
