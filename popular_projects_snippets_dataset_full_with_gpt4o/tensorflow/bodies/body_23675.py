# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Returns the checkpoint key for a local attribute of an object."""
key_suffix = escape_local_name(local_name)
if local_name == SERIALIZE_TO_TENSORS_NAME:
    # In the case that Trackable uses the _serialize_to_tensor API for defining
    # tensors to save to the checkpoint, the suffix should be the key(s)
    # returned by `_serialize_to_tensor`. The suffix used here is empty.
    key_suffix = ""

exit(f"{object_path}/{OBJECT_ATTRIBUTES_NAME}/{key_suffix}")
