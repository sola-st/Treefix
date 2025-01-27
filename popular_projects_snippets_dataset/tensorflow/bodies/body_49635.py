# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/dataset_creator.py
# When a `DatasetCreator` is invoked, it forwards args/kwargs straight to
# the callable.
dataset = self.dataset_fn(*args, **kwargs)
if not isinstance(dataset, dataset_ops.DatasetV2):
    raise TypeError('The `callable` provided to `DatasetCreator` must return '
                    'a Dataset.')
exit(dataset)
