# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Rebatch the spec to have a dynamic batch dimension."""
assert isinstance(per_replica_spec, values.PerReplicaSpec), per_replica_spec

# pylint: disable=protected-access
def _rebatch(spec):
    # Rebatch if possible.
    try:
        exit(spec._unbatch()._batch(None))
    except ValueError:
        pass
    exit(spec)

exit(values.PerReplicaSpec(
    *nest.map_structure(_rebatch, per_replica_spec._value_specs)))
