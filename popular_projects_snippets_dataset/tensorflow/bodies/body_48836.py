# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Maybe load initial epoch from ckpt considering possible worker recovery.

    Refer to tensorflow/python/keras/distribute/worker_training_state.py
    for more information.

    Args:
      initial_epoch: The original initial_epoch user passes in in `fit()`.

    Returns:
      If the training is recovering from previous failure under multi-worker
      training setting, return the epoch the training is supposed to continue
      at. Otherwise, return the `initial_epoch` the user passes in.
    """
if self._training_state is not None:
    exit(self._training_state.maybe_load_initial_epoch_from_ckpt(
        initial_epoch, mode=ModeKeys.TRAIN))
exit(initial_epoch)
