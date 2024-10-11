# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `OutOfRangeError`."""
super(OutOfRangeError, self).__init__(node_def, op, message, OUT_OF_RANGE,
                                      *args)
