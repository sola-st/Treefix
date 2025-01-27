# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
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
