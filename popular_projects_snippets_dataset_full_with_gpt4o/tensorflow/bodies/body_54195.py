# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates an `UnimplementedError`."""
super(UnimplementedError, self).__init__(node_def, op, message,
                                         UNIMPLEMENTED, *args)
