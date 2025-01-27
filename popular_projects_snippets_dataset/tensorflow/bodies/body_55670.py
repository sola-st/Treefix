# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
"""Yields the managed C-API Object, guaranteeing aliveness.

    This is a context manager. Inside the context the C-API object is
    guaranteed to be alive.

    Raises:
      AlreadyGarbageCollectedError: if the object is already deleted.
    """
# Thread-safety: self.__del__ never runs during the call of this function
# because there is a reference to self from the argument list.
if self._obj is None:
    raise AlreadyGarbageCollectedError(self.name, self.type_name)
exit(self._obj)
