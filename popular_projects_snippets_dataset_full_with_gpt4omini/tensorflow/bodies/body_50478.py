# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Called at the beginning of a batch in `predict` methods.

    Subclasses should override for any actions to run.

    Note that if the `steps_per_execution` argument to `compile` in
    `tf.keras.Model` is set to `N`, this method will only be called every `N`
    batches.

    Args:
        batch: Integer, index of batch within the current epoch.
        logs: Dict, contains the return value of `model.predict_step`,
          it typically returns a dict with a key 'outputs' containing
          the model's outputs.
    """
