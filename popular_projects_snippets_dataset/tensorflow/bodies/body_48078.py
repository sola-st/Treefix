# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Does validation on the compatibility of targets and loss functions.

  This helps prevent users from using loss functions incorrectly. This check
  is purely for UX purposes.

  Args:
      targets: list of Numpy arrays of targets.
      loss_fns: list of loss functions.
      output_shapes: list of shapes of model outputs.

  Raises:
      ValueError: if a loss function or target array
          is incompatible with an output.
  """
key_loss_fns = {
    losses.mean_squared_error, losses.binary_crossentropy,
    losses.categorical_crossentropy
}
key_loss_classes = (losses.MeanSquaredError, losses.BinaryCrossentropy,
                    losses.CategoricalCrossentropy)
for y, loss, shape in zip(targets, loss_fns, output_shapes):
    if y is None or loss is None or tensor_util.is_tf_type(y):
        continue
    if losses.is_categorical_crossentropy(loss):
        if y.shape[-1] == 1:
            raise ValueError('You are passing a target array of shape ' +
                             str(y.shape) +
                             ' while using as loss `categorical_crossentropy`. '
                             '`categorical_crossentropy` expects '
                             'targets to be binary matrices (1s and 0s) '
                             'of shape (samples, classes). '
                             'If your targets are integer classes, '
                             'you can convert them to the expected format via:\n'
                             '```\n'
                             'from keras.utils import to_categorical\n'
                             'y_binary = to_categorical(y_int)\n'
                             '```\n'
                             '\n'
                             'Alternatively, you can use the loss function '
                             '`sparse_categorical_crossentropy` instead, '
                             'which does expect integer targets.')

    is_loss_wrapper = isinstance(loss, losses.LossFunctionWrapper)
    if (isinstance(loss, key_loss_classes) or (is_loss_wrapper and
                                               (loss.fn in key_loss_fns))):
        for target_dim, out_dim in zip(y.shape[1:], shape[1:]):
            if out_dim is not None and target_dim != out_dim:
                loss_name = loss.name
                if loss_name is None:
                    loss_type = loss.fn if is_loss_wrapper else type(loss)
                    loss_name = loss_type.__name__
                raise ValueError('A target array with shape ' + str(y.shape) +
                                 ' was passed for an output of shape ' + str(shape) +
                                 ' while using as loss `' + loss_name + '`. '
                                 'This loss expects targets to have the same shape '
                                 'as the output.')
