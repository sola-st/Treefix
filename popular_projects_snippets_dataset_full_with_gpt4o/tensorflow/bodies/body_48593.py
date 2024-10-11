# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Validates `__init__` arguments."""
# Arguments that shouldn't be passed.
if not is_none_or_empty(y):
    raise ValueError("`y` argument is not supported when using "
                     "dataset as input.")
if not is_none_or_empty(sample_weights):
    raise ValueError("`sample_weight` argument is not supported when using "
                     "dataset as input.")

if steps is None:
    if _is_distributed_dataset(self._dataset):
        raise ValueError("When providing a distributed dataset, you must "
                         "specify the number of steps to run.")

    size = cardinality.cardinality(self._dataset).numpy()
    if size == cardinality.INFINITE and steps is None:
        raise ValueError(
            "When providing an infinite dataset, you must specify "
            "the number of steps to run (if you did not intend to "
            "create an infinite dataset, make sure to not call "
            "`repeat()` on the dataset).")
