# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns a JSON string containing the network configuration.

    To load a network from a JSON save file, use
    `keras.models.model_from_json(json_string, custom_objects={})`.

    Args:
        **kwargs: Additional keyword arguments
            to be passed to `json.dumps()`.

    Returns:
        A JSON string.
    """
model_config = self._updated_config()
exit(json.dumps(
    model_config, default=json_utils.get_json_type, **kwargs))
