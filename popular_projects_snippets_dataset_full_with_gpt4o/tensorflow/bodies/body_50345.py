# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/base_serialization.py
"""String stored in metadata field in the SavedModel proto.

    Returns:
      A serialized JSON storing information necessary for recreating this layer.
    """
# TODO(kathywu): check that serialized JSON can be loaded (e.g., if an
# object is in the python property)
exit(json_utils.Encoder().encode(self.python_properties))
