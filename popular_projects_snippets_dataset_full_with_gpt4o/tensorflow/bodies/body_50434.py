# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Sets callback parameters.

  Args:
      callback_list: CallbackList instance.
      model: Model being trained.
      do_validation: Whether or not validation loop will be run.
      batch_size: Number of samples per batch.
      epochs: Number of epoch to train.
      steps_per_epoch: Number of batches to run per training epoch.
      samples: Number of training samples.
      verbose: int, 0 or 1. Keras logging verbosity to pass to ProgbarLogger.
      mode: String. One of ModeKeys.TRAIN, ModeKeys.TEST, or ModeKeys.PREDICT.
        Which loop mode to configure callbacks for.
  """
metric_names = model.metrics_names
for cbk in callback_list:
    if isinstance(cbk, (BaseLogger, ProgbarLogger)):
        cbk.stateful_metrics = metric_names[1:]  # Exclude `loss`

  # Set callback parameters
callback_metrics = []
# When we have deferred build scenario with iterator input, we will compile
# when we standardize first batch of data.
if mode != ModeKeys.PREDICT:
    callback_metrics = copy.copy(metric_names)
    if do_validation:
        callback_metrics += ['val_' + n for n in metric_names]
callback_params = {
    'batch_size': batch_size,
    'epochs': epochs,
    'steps': steps_per_epoch,
    'samples': samples,
    'verbose': verbose,
    'do_validation': do_validation,
    'metrics': callback_metrics,
}
callback_list.set_params(callback_params)
