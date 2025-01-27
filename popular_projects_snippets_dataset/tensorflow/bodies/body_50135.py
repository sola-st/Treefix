# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Converts the weights between CuDNNGRU and GRU.

      Args:
        weights: Original weights.
        from_cudnn: Indicates whether original weights are from CuDNN layer.

      Returns:
        Updated weights compatible with GRU.
      """

kernels = transform_kernels(weights[0], transpose_input(from_cudnn),
                            n_gates)
recurrent_kernels = transform_kernels(weights[1], lambda k: k.T, n_gates)
biases = np.array(weights[2]).reshape((2, -1) if from_cudnn else -1)
exit([kernels, recurrent_kernels, biases])
