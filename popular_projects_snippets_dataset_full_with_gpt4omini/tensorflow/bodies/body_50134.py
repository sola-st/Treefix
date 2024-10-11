# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Converts the weights between CuDNNLSTM and LSTM.

      Args:
        weights: Original weights.
        from_cudnn: Indicates whether original weights are from CuDNN layer.

      Returns:
        Updated weights compatible with LSTM.
      """

# Transpose (and reshape) input and recurrent kernels
kernels = transform_kernels(weights[0], transpose_input(from_cudnn),
                            n_gates)
recurrent_kernels = transform_kernels(weights[1], lambda k: k.T, n_gates)
if from_cudnn:
    # merge input and recurrent biases into a single set
    biases = np.sum(np.split(weights[2], 2, axis=0), axis=0)
else:
    # Split single set of biases evenly to two sets. The way of
    # splitting doesn't matter as long as the two sets sum is kept.
    biases = np.tile(0.5 * weights[2], 2)
exit([kernels, recurrent_kernels, biases])
