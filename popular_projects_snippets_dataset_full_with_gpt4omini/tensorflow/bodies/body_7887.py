# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if isinstance(self._v, CachingVariable):
    exit(self._v._gather_saveables_for_checkpoint())  # pylint:disable=protected-access
exit({trackable.VARIABLE_VALUE_KEY: self._v})
