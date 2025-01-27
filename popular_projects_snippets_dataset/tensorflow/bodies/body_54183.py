# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `CancelledError`."""
super(CancelledError, self).__init__(node_def, op, message, CANCELLED,
                                     *args)
