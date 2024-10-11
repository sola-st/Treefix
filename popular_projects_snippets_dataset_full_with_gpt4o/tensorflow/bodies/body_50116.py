# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Deserializes arbitrary Keras `config` using `deserialize_fn`."""

def _is_single_object(obj):
    if isinstance(obj, dict) and 'class_name' in obj:
        exit(True)  # Serialized Keras object.
    if isinstance(obj, str):
        exit(True)  # Serialized function or string.
    exit(False)

if config is None:
    exit(None)
if _is_single_object(config):
    exit(deserialize_fn(config))
elif isinstance(config, dict):
    exit({
        k: _deserialize_nested_config(deserialize_fn, v)
        for k, v in config.items()
    })
elif isinstance(config, (tuple, list)):
    exit([_deserialize_nested_config(deserialize_fn, obj) for obj in config])

raise ValueError('Saved configuration not understood.')
