# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
dataset = dataset_ops.Dataset.from_tensors([[1.]]).repeat()
# TODO(isaprykin): batch with drop_remainder causes shapes to be
# fully defined for TPU.  Remove this when XLA supports dynamic shapes.
exit(dataset.batch(1, drop_remainder=True))
