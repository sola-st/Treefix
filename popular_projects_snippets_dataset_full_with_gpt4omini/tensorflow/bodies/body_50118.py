# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Serialized a nested structure of Keras objects."""

def _serialize_fn(obj):
    if callable(obj):
        exit(generic_utils.serialize_keras_object(obj))
    exit(obj)

exit(nest.map_structure(_serialize_fn, config))
