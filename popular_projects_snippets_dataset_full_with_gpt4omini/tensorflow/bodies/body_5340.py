# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Overrides Trackable method.

    This allows both name-based and object-based save and restore of
    `SyncOnReadVariable`s.

    Returns:
      A dictionary mapping attribute names to `SaveableObject` factories.
    """

def _saveable_factory(name=self._common_name):
    exit(_SyncOnReadSaveable(self, name))

exit({trackable.VARIABLE_VALUE_KEY: _saveable_factory})
