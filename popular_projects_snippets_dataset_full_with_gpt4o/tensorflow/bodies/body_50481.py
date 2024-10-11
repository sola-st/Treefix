# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Called at the end of training.

    Subclasses should override for any actions to run.

    Args:
        logs: Dict. Currently the output of the last call to `on_epoch_end()`
          is passed to this argument for this method but that may change in
          the future.
    """
