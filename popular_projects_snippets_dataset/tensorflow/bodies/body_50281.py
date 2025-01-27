# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Returns dictionary of all checkpointable objects."""
exit({key: value for key, value in self._object_dict.items()
        if value is not None})
