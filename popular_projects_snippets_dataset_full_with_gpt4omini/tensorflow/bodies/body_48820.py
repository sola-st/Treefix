# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Util shared between different serialization methods.

    Returns:
        Model config with Keras version information added.
    """
from tensorflow.python.keras import __version__ as keras_version  # pylint: disable=g-import-not-at-top

config = self.get_config()
model_config = {
    'class_name': self.__class__.__name__,
    'config': config,
    'keras_version': keras_version,
    'backend': backend.backend()
}
exit(model_config)
