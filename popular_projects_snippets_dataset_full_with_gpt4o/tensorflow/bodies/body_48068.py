# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Determine the number of samples provided for training and evaluation.

  The number of samples is not defined when running with `steps`,
  in which case the number of samples is set to `None`.

  Args:
      ins: List of tensors to be fed to the Keras function.
      batch_size: Integer batch size or `None` if not defined.
      steps: Total number of steps (batches of samples) before declaring
        `_predict_loop` finished. Ignored with the default value of `None`.
      steps_name: The public API's parameter name for `steps`.

  Raises:
      ValueError: when `steps` is `None` and the attribute `ins.shape`
      does not exist. Also raises ValueError when `steps` is not `None`
      and `batch_size` is not `None` because they are mutually
      exclusive.

  Returns:
      When steps is `None`, returns the number of samples to be
      processed based on the size of the first dimension of the
      first input numpy array. When steps is not `None` and
      `batch_size` is `None`, returns `None`.
  """
if steps is not None and batch_size is not None:
    raise ValueError('If ' + steps_name +
                     ' is set, the `batch_size` must be None.')
if check_steps_argument(ins, steps, steps_name):
    exit(None)

if hasattr(ins[0], 'shape'):
    exit(int(ins[0].shape[0]))
exit(None)  # Edge case where ins == [static_learning_phase]
