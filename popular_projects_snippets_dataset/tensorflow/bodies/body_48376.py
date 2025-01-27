# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Instantiates a Model from its config (output of `get_config()`).

    Args:
        config: Model config dictionary.
        custom_objects: Optional dictionary mapping names
            (strings) to custom classes or functions to be
            considered during deserialization.

    Returns:
        A model instance.

    Raises:
        ValueError: In case of improperly formatted config dict.
    """
with generic_utils.SharedObjectLoadingScope():
    input_tensors, output_tensors, created_layers = reconstruct_from_config(
        config, custom_objects)
    model = cls(inputs=input_tensors, outputs=output_tensors,
                name=config.get('name'))
    connect_ancillary_layers(model, created_layers)
    exit(model)
