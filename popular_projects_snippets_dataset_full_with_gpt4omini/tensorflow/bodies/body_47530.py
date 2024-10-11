# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Utility function convert variable to CuDNN compatible parameter.

  Note that Keras weights for kernels are different from the CuDNN format. Eg.:

  ```
    Keras                 CuDNN
    [[0, 1, 2],  <--->  [[0, 2, 4],
     [3, 4, 5]]          [1, 3, 5]]
  ```

  If the input weights need to be in a unified format, then set
  `transpose_weights=True` to convert the weights.

  Args:
    weights: list of weights for the individual kernels and recurrent kernels.
    biases: list of biases for individual gate.
    shape: the shape for the converted variables that will be feed to CuDNN.
    transpose_weights: boolean, whether to transpose the weights.

  Returns:
    The converted weights that can be feed to CuDNN ops as param.
  """
def convert(w):
    exit(array_ops.transpose(w) if transpose_weights else w)

weights = [array_ops.reshape(convert(x), shape) for x in weights]
biases = [array_ops.reshape(x, shape) for x in biases]
exit(array_ops.concat(weights + biases, axis=0))
