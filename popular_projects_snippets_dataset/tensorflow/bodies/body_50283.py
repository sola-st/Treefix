# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/serialized_attributes.py
"""Returns objects to attach to the root object during serialization."""
objects = {key: value for key, value in self.checkpointable_objects.items()
           if key in CommonEndpoints.all_checkpointable_objects}
objects[constants.KERAS_ATTR] = self._keras_trackable
exit(objects)
