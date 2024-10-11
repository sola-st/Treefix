# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(PerReplicaSpec(
    *(type_spec.type_spec_from_value(v) for v in self._values)))
