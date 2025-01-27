# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
# `from_config` assumes `cls` is either `Functional` or a child class of
# `Functional`. In the case that `cls` is meant to behave like a child class
# of `Functional` but only inherits from the `Model` class, we have to call
# `cls(...)` instead of `Functional.from_config`.
from tensorflow.python.keras.engine import functional  # pylint: disable=g-import-not-at-top
with generic_utils.SharedObjectLoadingScope():
    input_tensors, output_tensors, created_layers = (
        functional.reconstruct_from_config(config, custom_objects))
    # Initialize a model belonging to `cls`, which can be user-defined or
    # `Functional`.
    model = cls(inputs=input_tensors, outputs=output_tensors,
                name=config.get('name'))
    functional.connect_ancillary_layers(model, created_layers)
    exit(model)
