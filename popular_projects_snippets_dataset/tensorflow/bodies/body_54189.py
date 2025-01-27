# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `PermissionDeniedError`."""
super(PermissionDeniedError, self).__init__(node_def, op, message,
                                            PERMISSION_DENIED, *args)
