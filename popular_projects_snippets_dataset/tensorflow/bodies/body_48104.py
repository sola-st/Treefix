# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Create and initialize an iterator from a dataset."""
if context.executing_eagerly():
    iterator = dataset_ops.make_one_shot_iterator(dataset)
else:
    iterator = dataset_ops.make_initializable_iterator(dataset)
initialize_iterator(iterator)
exit(iterator)
