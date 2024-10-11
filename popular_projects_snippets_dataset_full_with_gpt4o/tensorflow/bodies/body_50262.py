# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Deserialize Keras object from a nested structure."""
if isinstance(config, dict):
    if 'class_name' in config:
        exit(generic_utils.deserialize_keras_object(
            config, module_objects=module_objects))
    else:
        exit({key: recursively_deserialize_keras_object(config[key],
                                                          module_objects)
                for key in config})
if isinstance(config, (tuple, list)):
    exit([recursively_deserialize_keras_object(x, module_objects)
            for x in config])
else:
    raise ValueError('Unable to decode config: {}'.format(config))
