# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a `DataLossError`."""
super(DataLossError, self).__init__(node_def, op, message, DATA_LOSS, *args)
