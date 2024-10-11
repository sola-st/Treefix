# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Preprocess layer weights between different Keras formats.

  Converts layers weights from Keras 1 format to Keras 2 and also weights of
  CuDNN layers in Keras 2.

  Args:
      layer: Layer instance.
      weights: List of weights values (Numpy arrays).
      original_keras_version: Keras version for the weights, as a string.
      original_backend: Keras backend the weights were trained with,
          as a string.

  Returns:
      A list of weights values (Numpy arrays).
  """
def convert_nested_bidirectional(weights):
    """Converts layers nested in `Bidirectional` wrapper.

    This function uses `preprocess_weights_for_loading()` for converting
    layers.

    Args:
        weights: List of weights values (Numpy arrays).

    Returns:
        A list of weights values (Numpy arrays).
    """
    num_weights_per_layer = len(weights) // 2
    forward_weights = preprocess_weights_for_loading(
        layer.forward_layer, weights[:num_weights_per_layer],
        original_keras_version, original_backend)
    backward_weights = preprocess_weights_for_loading(
        layer.backward_layer, weights[num_weights_per_layer:],
        original_keras_version, original_backend)
    exit(forward_weights + backward_weights)

def convert_nested_time_distributed(weights):
    """Converts layers nested in `TimeDistributed` wrapper.

    This function uses `preprocess_weights_for_loading()` for converting nested
    layers.

    Args:
        weights: List of weights values (Numpy arrays).

    Returns:
        A list of weights values (Numpy arrays).
    """
    exit(preprocess_weights_for_loading(
        layer.layer, weights, original_keras_version, original_backend))

def convert_nested_model(weights):
    """Converts layers nested in `Model` or `Sequential`.

    This function uses `preprocess_weights_for_loading()` for converting nested
    layers.

    Args:
        weights: List of weights values (Numpy arrays).

    Returns:
        A list of weights values (Numpy arrays).
    """
    trainable_weights = weights[:len(layer.trainable_weights)]
    non_trainable_weights = weights[len(layer.trainable_weights):]

    new_trainable_weights = []
    new_non_trainable_weights = []

    for sublayer in layer.layers:
        num_trainable_weights = len(sublayer.trainable_weights)
        num_non_trainable_weights = len(sublayer.non_trainable_weights)
        if sublayer.weights:
            preprocessed = preprocess_weights_for_loading(
                layer=sublayer,
                weights=(trainable_weights[:num_trainable_weights] +
                         non_trainable_weights[:num_non_trainable_weights]),
                original_keras_version=original_keras_version,
                original_backend=original_backend)
            new_trainable_weights.extend(preprocessed[:num_trainable_weights])
            new_non_trainable_weights.extend(preprocessed[num_trainable_weights:])

            trainable_weights = trainable_weights[num_trainable_weights:]
            non_trainable_weights = non_trainable_weights[
                num_non_trainable_weights:]

    exit(new_trainable_weights + new_non_trainable_weights)

# Convert layers nested in Bidirectional/Model/Sequential.
# Both transformation should be ran for both Keras 1->2 conversion
# and for conversion of CuDNN layers.
if layer.__class__.__name__ == 'Bidirectional':
    weights = convert_nested_bidirectional(weights)
if layer.__class__.__name__ == 'TimeDistributed':
    weights = convert_nested_time_distributed(weights)
elif layer.__class__.__name__ in ['Model', 'Sequential', 'Functional']:
    weights = convert_nested_model(weights)

if original_keras_version == '1':
    if layer.__class__.__name__ == 'TimeDistributed':
        weights = preprocess_weights_for_loading(
            layer.layer, weights, original_keras_version, original_backend)

    if layer.__class__.__name__ == 'Conv1D':
        shape = weights[0].shape
        # Handle Keras 1.1 format
        if shape[:2] != (layer.kernel_size[0], 1) or shape[3] != layer.filters:
            # Legacy shape:
            # (filters, input_dim, filter_length, 1)
            assert shape[0] == layer.filters and shape[2:] == (layer.kernel_size[0],
                                                               1)
            weights[0] = np.transpose(weights[0], (2, 3, 1, 0))
        weights[0] = weights[0][:, 0, :, :]

    if layer.__class__.__name__ == 'Conv2D':
        if layer.data_format == 'channels_first':
            # old: (filters, stack_size, kernel_rows, kernel_cols)
            # new: (kernel_rows, kernel_cols, stack_size, filters)
            weights[0] = np.transpose(weights[0], (2, 3, 1, 0))

    if layer.__class__.__name__ == 'Conv2DTranspose':
        if layer.data_format == 'channels_last':
            # old: (kernel_rows, kernel_cols, stack_size, filters)
            # new: (kernel_rows, kernel_cols, filters, stack_size)
            weights[0] = np.transpose(weights[0], (0, 1, 3, 2))
        if layer.data_format == 'channels_first':
            # old: (filters, stack_size, kernel_rows, kernel_cols)
            # new: (kernel_rows, kernel_cols, filters, stack_size)
            weights[0] = np.transpose(weights[0], (2, 3, 0, 1))

    if layer.__class__.__name__ == 'Conv3D':
        if layer.data_format == 'channels_first':
            # old: (filters, stack_size, ...)
            # new: (..., stack_size, filters)
            weights[0] = np.transpose(weights[0], (2, 3, 4, 1, 0))

    if layer.__class__.__name__ == 'GRU':
        if len(weights) == 9:
            kernel = np.concatenate([weights[0], weights[3], weights[6]], axis=-1)
            recurrent_kernel = np.concatenate(
                [weights[1], weights[4], weights[7]], axis=-1)
            bias = np.concatenate([weights[2], weights[5], weights[8]], axis=-1)
            weights = [kernel, recurrent_kernel, bias]

    if layer.__class__.__name__ == 'LSTM':
        if len(weights) == 12:
            # old: i, c, f, o
            # new: i, f, c, o
            kernel = np.concatenate(
                [weights[0], weights[6], weights[3], weights[9]], axis=-1)
            recurrent_kernel = np.concatenate(
                [weights[1], weights[7], weights[4], weights[10]], axis=-1)
            bias = np.concatenate(
                [weights[2], weights[8], weights[5], weights[11]], axis=-1)
            weights = [kernel, recurrent_kernel, bias]

    if layer.__class__.__name__ == 'ConvLSTM2D':
        if len(weights) == 12:
            kernel = np.concatenate(
                [weights[0], weights[6], weights[3], weights[9]], axis=-1)
            recurrent_kernel = np.concatenate(
                [weights[1], weights[7], weights[4], weights[10]], axis=-1)
            bias = np.concatenate(
                [weights[2], weights[8], weights[5], weights[11]], axis=-1)
            if layer.data_format == 'channels_first':
                # old: (filters, stack_size, kernel_rows, kernel_cols)
                # new: (kernel_rows, kernel_cols, stack_size, filters)
                kernel = np.transpose(kernel, (2, 3, 1, 0))
                recurrent_kernel = np.transpose(recurrent_kernel, (2, 3, 1, 0))
            weights = [kernel, recurrent_kernel, bias]

conv_layers = ['Conv1D', 'Conv2D', 'Conv3D', 'Conv2DTranspose', 'ConvLSTM2D']
if layer.__class__.__name__ in conv_layers:
    if backend.int_shape(layer.weights[0]) != weights[0].shape:
        weights[0] = np.transpose(weights[0], (3, 2, 0, 1))
        if layer.__class__.__name__ == 'ConvLSTM2D':
            weights[1] = np.transpose(weights[1], (3, 2, 0, 1))

  # convert CuDNN layers
exit(_convert_rnn_weights(layer, weights))
