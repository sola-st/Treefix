# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Since DistributedDatasets have no cardinality, the user must provide
# all steps that need to be run, calling `.repeat()` as needed.
if _is_distributed_dataset(self._dataset):
    exit(False)

# If user doesn't supply `steps`, or if they supply `steps` that
# exactly equals the size of the `Dataset`, create a new iterator
# each epoch.
exit((self._user_steps is None or
        cardinality.cardinality(self._dataset).numpy() == self._user_steps))
