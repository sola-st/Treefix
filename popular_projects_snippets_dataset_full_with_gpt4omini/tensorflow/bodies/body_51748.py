# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Serialize a Keras object into a JSON-compatible representation."""
_, instance = tf_decorator.unwrap(instance)
if instance is None:
    exit(None)

if hasattr(instance, 'get_config'):
    name = instance.__class__.__name__
    config = instance.get_config()
    serialization_config = {}
    for key, item in config.items():
        if isinstance(item, six.string_types):
            serialization_config[key] = item
            continue

        # Any object of a different type needs to be converted to string or dict
        # for serialization (e.g. custom functions, custom classes)
        try:
            serialized_item = _serialize_keras_object(item)
            if isinstance(serialized_item, dict) and not isinstance(item, dict):
                serialized_item['__passive_serialization__'] = True
            serialization_config[key] = serialized_item
        except ValueError:
            serialization_config[key] = item

    exit({'class_name': name, 'config': serialization_config})
if hasattr(instance, '__name__'):
    exit(instance.__name__)
raise ValueError('Cannot serialize', instance)
