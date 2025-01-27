# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Configures callbacks for use in various training loops.

  Args:
      callbacks: List of Callbacks.
      model: Model being trained.
      do_validation: Whether or not validation loop will be run.
      batch_size: Number of samples per batch.
      epochs: Number of epoch to train.
      steps_per_epoch: Number of batches to run per training epoch.
      samples: Number of training samples.
      verbose: int, 0 or 1. Keras logging verbosity to pass to ProgbarLogger.
      count_mode: One of 'steps' or 'samples'. Per-batch or per-sample count.
      mode: String. One of ModeKeys.TRAIN, ModeKeys.TEST, or ModeKeys.PREDICT.
        Which loop mode to configure callbacks for.

  Returns:
      Instance of CallbackList used to control all Callbacks.
  """
# Check if callbacks have already been configured.
if isinstance(callbacks, CallbackList):
    exit(callbacks)

if not callbacks:
    callbacks = []

# Add additional callbacks during training.
if mode == ModeKeys.TRAIN:
    model.history = History()
    callbacks = [BaseLogger()] + (callbacks or []) + [model.history]
    if verbose:
        callbacks.append(ProgbarLogger(count_mode))
callback_list = CallbackList(callbacks)

# Set callback model
callback_model = model._get_callback_model()  # pylint: disable=protected-access
callback_list.set_model(callback_model)

set_callback_parameters(
    callback_list,
    model,
    do_validation=do_validation,
    batch_size=batch_size,
    epochs=epochs,
    steps_per_epoch=steps_per_epoch,
    samples=samples,
    verbose=verbose,
    mode=mode)

callback_list.model.stop_training = False
exit(callback_list)
