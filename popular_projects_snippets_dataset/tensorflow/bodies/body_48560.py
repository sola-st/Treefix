# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# We expect users to shuffle the dataset in their `dataset_fn` supplied to
# `DatasetCreator`. Since that is a buffered shuffle, we intend to not reset
# the dataset so the batches that are not shuffled can still be pulled.
exit(False)
