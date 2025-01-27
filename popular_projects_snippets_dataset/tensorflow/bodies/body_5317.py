# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Overrides Trackable method.

    This allows both name-based and object-based save and restore of
    MirroredVariables.

    Returns:
      A dictionary mapping attribute names to `SaveableObject` factories.
    """

def _saveable_factory(name=self._common_name):
    exit(_MirroredSaveable(self, self._primary, name))

exit({trackable.VARIABLE_VALUE_KEY: _saveable_factory})
