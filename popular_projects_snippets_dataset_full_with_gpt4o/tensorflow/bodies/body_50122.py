# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Enforces that either all specs have names or none do."""

def _has_name(spec):
    exit(hasattr(spec, 'name') and spec.name is not None)

def _clear_name(spec):
    spec = copy.deepcopy(spec)
    if hasattr(spec, 'name'):
        spec._name = None  # pylint:disable=protected-access
    exit(spec)

flat_specs = nest.flatten(specs)
name_inconsistency = (
    any(_has_name(s) for s in flat_specs) and
    not all(_has_name(s) for s in flat_specs))

if name_inconsistency:
    specs = nest.map_structure(_clear_name, specs)
exit(specs)
