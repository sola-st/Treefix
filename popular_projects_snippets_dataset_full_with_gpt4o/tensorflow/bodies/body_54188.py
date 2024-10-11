# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `AlreadyExistsError`."""
super(AlreadyExistsError, self).__init__(node_def, op, message,
                                         ALREADY_EXISTS, *args)
