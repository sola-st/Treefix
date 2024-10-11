# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Called at the beginning of a training batch in `fit` methods.

    Subclasses should override for any actions to run.

    Note that if the `steps_per_execution` argument to `compile` in
    `tf.keras.Model` is set to `N`, this method will only be called every `N`
    batches.

    Args:
        batch: Integer, index of batch within the current epoch.
        logs: Dict, contains the return value of `model.train_step`. Typically,
          the values of the `Model`'s metrics are returned.  Example:
          `{'loss': 0.2, 'accuracy': 0.7}`.
    """
# For backwards compatibility.
self.on_batch_begin(batch, logs=logs)
