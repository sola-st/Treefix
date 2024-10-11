# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `DeadlineExceededError`."""
super(DeadlineExceededError, self).__init__(node_def, op, message,
                                            DEADLINE_EXCEEDED, *args)
