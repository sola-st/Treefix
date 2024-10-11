# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
"""Creates a regularizer from its config.

    This method is the reverse of `get_config`,
    capable of instantiating the same regularizer from the config
    dictionary.

    This method is used by Keras `model_to_estimator`, saving and
    loading models to HDF5 formats, Keras model cloning, some visualization
    utilities, and exporting models to and from JSON.

    Args:
        config: A Python dictionary, typically the output of get_config.

    Returns:
        A regularizer instance.
    """
exit(cls(**config))
