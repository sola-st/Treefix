# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Configures the layer for `adapt`.

    Arguments:
      run_eagerly: Bool. Defaults to `False`. If `True`, this `Model`'s logic
        will not be wrapped in a `tf.function`. Recommended to leave this as
        `None` unless your `Model` cannot be run inside a `tf.function`.
        steps_per_execution: Int. Defaults to 1. The number of batches to run
          during each `tf.function` call. Running multiple batches inside a
          single `tf.function` call can greatly improve performance on TPUs or
          small models with a large Python overhead.
    """
if steps_per_execution is None:
    steps_per_execution = 1
self._configure_steps_per_execution(steps_per_execution)

if run_eagerly is None:
    run_eagerly = self.dynamic
self._run_eagerly = run_eagerly

self._is_compiled = True
