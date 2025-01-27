# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `FailedPreconditionError`."""
super(FailedPreconditionError, self).__init__(node_def, op, message,
                                              FAILED_PRECONDITION, *args)
