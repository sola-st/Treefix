# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `AbortedError`."""
super(AbortedError, self).__init__(node_def, op, message, ABORTED, *args)
