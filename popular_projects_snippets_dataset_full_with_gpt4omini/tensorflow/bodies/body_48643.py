# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if not isinstance(x, dataset_creator.DatasetCreator):
    raise TypeError("When using `ParameterServerStrategy`, `x` must be a "
                    "`DatasetCreator`.")

def per_worker_dataset_fn():

    exit(strategy.distribute_datasets_from_function(
        x, options=x.input_options))

self._dataset = self._model._cluster_coordinator.create_per_worker_dataset(  # pylint: disable=protected-access
    per_worker_dataset_fn)

if steps_per_epoch == -1:
    self._inferred_steps = None
    self._log_indefinite_training_warning()
else:
    self._inferred_steps = steps_per_epoch
