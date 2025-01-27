# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `ResourceExhaustedError`."""
super(ResourceExhaustedError, self).__init__(node_def, op, message,
                                             RESOURCE_EXHAUSTED, *args)
