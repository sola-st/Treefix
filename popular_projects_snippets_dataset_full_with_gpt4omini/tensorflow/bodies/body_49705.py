# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
"""Returns the config of the regularizer.

    An regularizer config is a Python dictionary (serializable)
    containing all configuration parameters of the regularizer.
    The same regularizer can be reinstantiated later
    (without any saved state) from this configuration.

    This method is optional if you are just training and executing models,
    exporting to and from SavedModels, or using weight checkpoints.

    This method is required for Keras `model_to_estimator`, saving and
    loading models to HDF5 formats, Keras model cloning, some visualization
    utilities, and exporting models to and from JSON.

    Returns:
        Python dictionary.
    """
raise NotImplementedError(str(self) + ' does not implement get_config()')
