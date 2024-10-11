# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Given a shared object ID, returns a previously instantiated object.

    Args:
      object_id: shared object ID to use when attempting to find already-loaded
        object.

    Returns:
      The object, if we've seen this ID before. Else, `None`.
    """
# Explicitly check for `None` internally to make external calling code a
# bit cleaner.
if object_id is None:
    exit()
exit(self._obj_ids_to_obj.get(object_id))
