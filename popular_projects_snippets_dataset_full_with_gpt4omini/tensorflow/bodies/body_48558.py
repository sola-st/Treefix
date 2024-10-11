# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
super(DatasetCreatorAdapter, self).__init__(x, **kwargs)

if not isinstance(x, dataset_creator.DatasetCreator):
    raise TypeError("The input of a `DatasetCreatorAdapter` should be a "
                    "`DatasetCreator` but it received type {}.".format(
                        type(x)))
if steps is None:
    raise ValueError("When using a "
                     "`tf.keras.utils.experimental.DatasetCreator`, "
                     "`steps_per_epoch`, `validation_steps` or `steps` "
                     "argument must be provided in `Model.fit`, "
                     "`Model.evaluate`, or `Model.predict`.")
self.dataset_creator = x
self.steps = steps
self.strategy = distribution_strategy
