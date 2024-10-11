# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Saves objects to a dictionary, and validates the values."""
for key in self.all_checkpointable_objects:
    if key in object_dict:
        if not isinstance(object_dict[key], trackable.Trackable):
            raise ValueError(
                'Object dictionary contained a non-trackable object: {} (for key'
                ' {})'.format(object_dict[key], key))
        self._object_dict[key] = object_dict[key]
        setattr(self._keras_trackable, key, object_dict[key])
    else:
        raise ValueError(
            'Object {} missing from serialized object dict.'.format(key))
exit(self.checkpointable_objects)
