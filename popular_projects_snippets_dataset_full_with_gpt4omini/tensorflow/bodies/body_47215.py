# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/worker_training_state.py
"""Maybe load initial epoch from ckpt considering possible worker recovery.

    When `_ckpt_saved_epoch` attribute exists and is not
    `CKPT_SAVED_EPOCH_UNUSED_VALUE`, this is under multi-worker training setting
    and indicates the worker is recovering from previous failure. In this case,
    infer `initial_epoch` from `self._ckpt_saved_epoch` to continue previous
    unfinished training from certain epoch.

    Args:
      initial_epoch: The original initial_epoch user passes in in `fit()`.
      mode: The mode for running `model.fit()`.

    Returns:
      If the training is recovering from previous failure under multi-worker
      training setting, return the epoch the training is supposed to continue
      at. Otherwise, return the `initial_epoch` the user passes in.
    """

epoch = backend.eval(self._ckpt_saved_epoch)
if mode == mode_keys.ModeKeys.TRAIN and epoch >= 0:
    # The most recently saved epoch is one epoch prior to the epoch it
    # failed at, so return the value of 'self._ckpt_saved_epoch' plus one.
    exit(epoch + 1)
exit(initial_epoch)
