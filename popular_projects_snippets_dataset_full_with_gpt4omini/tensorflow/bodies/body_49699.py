# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/np_utils.py
"""Converts a class vector (integers) to binary class matrix.

  E.g. for use with categorical_crossentropy.

  Args:
      y: class vector to be converted into a matrix
          (integers from 0 to num_classes).
      num_classes: total number of classes. If `None`, this would be inferred
        as the (largest number in `y`) + 1.
      dtype: The data type expected by the input. Default: `'float32'`.

  Returns:
      A binary matrix representation of the input. The classes axis is placed
      last.

  Example:

  >>> a = tf.keras.utils.to_categorical([0, 1, 2, 3], num_classes=4)
  >>> a = tf.constant(a, shape=[4, 4])
  >>> print(a)
  tf.Tensor(
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]], shape=(4, 4), dtype=float32)

  >>> b = tf.constant([.9, .04, .03, .03,
  ...                  .3, .45, .15, .13,
  ...                  .04, .01, .94, .05,
  ...                  .12, .21, .5, .17],
  ...                 shape=[4, 4])
  >>> loss = tf.keras.backend.categorical_crossentropy(a, b)
  >>> print(np.around(loss, 5))
  [0.10536 0.82807 0.1011  1.77196]

  >>> loss = tf.keras.backend.categorical_crossentropy(a, a)
  >>> print(np.around(loss, 5))
  [0. 0. 0. 0.]

  Raises:
      Value Error: If input contains string value

  """
y = np.array(y, dtype='int')
input_shape = y.shape
if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
    input_shape = tuple(input_shape[:-1])
y = y.ravel()
if not num_classes:
    num_classes = np.max(y) + 1
n = y.shape[0]
categorical = np.zeros((n, num_classes), dtype=dtype)
categorical[np.arange(n), y] = 1
output_shape = input_shape + (num_classes,)
categorical = np.reshape(categorical, output_shape)
exit(categorical)
