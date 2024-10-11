# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Raises errors if arguments are invalid.

  Args:
    is_sequence: Boolean, whether data is a `keras.utils.data_utils.Sequence`
      instance.
    is_dataset: Boolean, whether data is a dataset instance.
    use_multiprocessing: Boolean. If `True`, use process-based threading. If
      unspecified, `use_multiprocessing` will default to `False`. Note that
      because this implementation relies on multiprocessing, you should not pass
      non-picklable arguments to the generator as they can't be passed easily to
      children processes.
    workers: Integer. Maximum number of processes to spin up when using
      process-based threading. If unspecified, `workers` will default to 1. If
      0, will execute the generator on the main thread.
    steps_per_epoch: Total number of steps (batches of samples) before declaring
      one epoch finished and starting the next epoch. Ignored with the default
      value of `None`.
    validation_data: Either a tuple of NumPy/Tensor inputs (i.e. `(x,)` or `(x,
      y)` or `(x, y, sample_weights)`) or a generator or
      `keras.utils.data_utils.Sequence` object or Eager Iterator or Dataset.
    validation_steps: Total number of steps (batches of samples) before
      declaring validation finished.
    mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.
    kwargs: Additional arguments for backwards compatibility.

  Raises:
    ValueError: If `steps_per_epoch` or `validation_steps` are not passed
      for data types that require them, or if unrecognized keyword
      arguments are passed.
  """
if not is_sequence and use_multiprocessing and workers > 1:
    logging.warning(
        UserWarning('Using a generator with `use_multiprocessing=True`'
                    ' and multiple workers may duplicate your data.'
                    ' Please consider using the `keras.utils.Sequence`'
                    ' class.'))

if steps_per_epoch is None and not is_dataset:
    arg_name = 'steps_per_epoch' if mode == ModeKeys.TRAIN else 'steps'
    raise ValueError('Please specify the number of steps via the '
                     '`{}` argument.'.format(arg_name))

val_gen = (
    data_utils.is_generator_or_sequence(validation_data) or
    isinstance(validation_data, iterator_ops.IteratorBase))
if (val_gen and not isinstance(validation_data, data_utils.Sequence) and
    not validation_steps):
    raise ValueError('Please specify the `validation_steps` argument.')

if any(k != 'steps' for k in kwargs):
    raise ValueError('Invalid arguments passed: {}'.format(
        [k for k in kwargs if k != 'steps']))
