# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Creates a layer from its config.

    This method is the reverse of `get_config`,
    capable of instantiating the same layer from the config
    dictionary. It does not handle layer connectivity
    (handled by Network), nor weights (handled by `set_weights`).

    Args:
        config: A Python dictionary, typically the
            output of get_config.

    Returns:
        A layer instance.
    """
exit(cls(**config))
