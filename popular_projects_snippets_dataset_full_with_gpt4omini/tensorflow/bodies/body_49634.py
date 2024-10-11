# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/dataset_creator.py
if not callable(dataset_fn):
    raise TypeError('`dataset_fn` for `DatasetCreator` must be a `callable`.')
if input_options and (not isinstance(input_options,
                                     distribute_lib.InputOptions)):
    raise TypeError('`input_options` for `DatasetCreator` must be a '
                    '`tf.distribute.InputOptions`.')

self.dataset_fn = dataset_fn
self.input_options = input_options
