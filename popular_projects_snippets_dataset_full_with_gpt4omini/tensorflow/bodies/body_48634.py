# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Catch OutOfRangeError for Datasets of unknown size.
# This blocks until the batch has finished executing.
# TODO(b/150292341): Allow multiple async steps here.
exit(self._inferred_steps is None)
