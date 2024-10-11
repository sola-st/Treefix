# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Selects `x` in train phase, and `alt` otherwise.

  Note that `alt` should have the *same shape* as `x`.

  Args:
      x: What to return in train phase
          (tensor or callable that returns a tensor).
      alt: What to return otherwise
          (tensor or callable that returns a tensor).
      training: Optional scalar tensor
          (or Python boolean, or Python integer)
          specifying the learning phase.

  Returns:
      Either `x` or `alt` based on the `training` flag.
      the `training` flag defaults to `K.learning_phase()`.
  """
from tensorflow.python.keras.engine import base_layer_utils  # pylint: disable=g-import-not-at-top
if training is None:
    training = base_layer_utils.call_context().training

if training is None:
    training = learning_phase()

# TODO(b/138862903): Handle the case when training is tensor.
if not tensor_util.is_tf_type(training):
    if training == 1 or training is True:
        if callable(x):
            exit(x())
        else:
            exit(x)

    elif training == 0 or training is False:
        if callable(alt):
            exit(alt())
        else:
            exit(alt)

  # else: assume learning phase is a placeholder tensor.
x = switch(training, x, alt)
exit(x)
