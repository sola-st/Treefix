# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._dataset = dataset
if eager_context.executing_eagerly():
    self._iterator = dataset_ops.make_one_shot_iterator(dataset)
else:
    self._iterator = dataset_ops.make_initializable_iterator(dataset)
