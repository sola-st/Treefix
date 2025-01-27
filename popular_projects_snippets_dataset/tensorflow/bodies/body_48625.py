# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Initializes a `DataHandler`.

    Arguments:
      x: See `Model.fit`.
      y: See `Model.fit`.
      sample_weight: See `Model.fit`.
      batch_size: See `Model.fit`.
      steps_per_epoch: See `Model.fit`.
      initial_epoch: See `Model.fit`.
      epochs: See `Model.fit`.
      shuffle: See `Model.fit`.
      class_weight: See `Model.fit`.
      max_queue_size: See `Model.fit`.
      workers: See `Model.fit`.
      use_multiprocessing: See `Model.fit`.
      model: The `Model` instance. Needed in order to correctly `build` the
        `Model` using generator-like inputs (see `GeneratorDataAdapter`).
      steps_per_execution: See `Model.compile`.
      distribute: Whether to distribute the `tf.dataset`.
        `PreprocessingLayer.adapt` does not support distributed datasets,
        `Model` should always set this to `True`.
    """

self._initial_epoch = initial_epoch
self._epochs = epochs
self._insufficient_data = False
self._model = model

# `steps_per_execution_value` is the cached initial value.
# `steps_per_execution` is mutable and may be changed by the DataAdapter
# to handle partial executions.
if steps_per_execution is None:
    self._steps_per_execution = 1
    self._steps_per_execution_value = 1
else:
    self._steps_per_execution = steps_per_execution
    self._steps_per_execution_value = steps_per_execution.numpy().item()

adapter_cls = select_data_adapter(x, y)
self._adapter = adapter_cls(
    x,
    y,
    batch_size=batch_size,
    steps=steps_per_epoch,
    epochs=epochs - initial_epoch,
    sample_weights=sample_weight,
    shuffle=shuffle,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    distribution_strategy=ds_context.get_strategy(),
    model=model)

strategy = ds_context.get_strategy()

self._current_step = 0
self._step_increment = self._steps_per_execution_value - 1
self._insufficient_data = False

self._configure_dataset_and_inferred_steps(strategy, x, steps_per_epoch,
                                           class_weight, distribute)
