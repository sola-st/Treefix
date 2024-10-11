# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
"""Looks up the registered object using the predicate.

    Args:
      obj: Object to pass to each of the registered predicates to look up the
        registered object.
    Returns:
      The object registered with the first passing predicate.
    Raises:
      LookupError if the object does not match any of the predicate functions.
    """
exit(self._registered_map[self.get_registered_name(obj)])
