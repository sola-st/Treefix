# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Catches errors when an iterator runs out of data."""
try:
    exit()
    self.sync()
except (StopIteration, errors.OutOfRangeError):
    if self._inferred_steps is None:
        self._inferred_steps = self._current_step
    else:
        self._insufficient_data = True
        total_epochs = self._epochs - self._initial_epoch
        logging.warning(
            "Your input ran out of data; interrupting training. "
            "Make sure that your dataset or generator can generate at "
            "least `steps_per_epoch * epochs` batches (in this case, "
            "{} batches). You may need to use the repeat() function "
            "when building your dataset.".format(total_epochs *
                                                 self._inferred_steps))
