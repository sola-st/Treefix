# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Check whether the input tensors are with supported dtypes.

  Default RNN cells only support floats and complex as its dtypes since the
  activation function (tanh and sigmoid) only allow those types. This function
  will throw a proper error message if the inputs is not in a supported type.

  Args:
    inputs: tensor or nested structure of tensors that are feed to RNN cell as
      input or state.

  Raises:
    ValueError: if any of the input tensor are not having dtypes of float or
      complex.
  """
for t in nest.flatten(inputs):
    _check_supported_dtypes(t.dtype)
