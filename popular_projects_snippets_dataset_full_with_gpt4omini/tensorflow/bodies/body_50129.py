# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
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
