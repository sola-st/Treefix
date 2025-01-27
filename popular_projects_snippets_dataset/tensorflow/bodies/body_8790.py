# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
exit(PerWorkerValuesTypeSpec(
    self._values[0]._type_spec,  # pylint: disable=protected-access
    type(self)))
