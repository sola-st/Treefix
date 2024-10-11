group = False # pragma: no cover
def regroup(updates, grouped_mirrored): return updates # pragma: no cover
updates = [] # pragma: no cover
nest = type('Mock', (object,), {'map_structure': lambda self, f, x: x})() # pragma: no cover
extended = type('Mock', (object,), {'_local_results': lambda: []})() # pragma: no cover
ops = type('Mock', (object,), {'device': lambda x: None, 'control_dependencies': lambda xs: xs})() # pragma: no cover

group = False # pragma: no cover
def regroup(updates, grouped_mirrored): return updates # pragma: no cover
values_lib = type('MockValuesLib', (), {'Mirrored': lambda x: f'Mirrored({x})'})() # pragma: no cover
nest = type('MockNest', (), {'map_structure': lambda self, fn, struct: [fn(item) for item in struct]})() # pragma: no cover
extended = type('MockExtended', (), {'_local_results': lambda: 'local_results_placeholder'})() # pragma: no cover
ops = type('MockOps', (), {'device': lambda x: x, 'control_dependencies': lambda deps: deps})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
from l3.Runtime import _l_
"""Regroup for an update, with dependencies to ensure all updates execute."""
if not group:
    _l_(5920)

    regrouped = regroup(updates, values_lib.Mirrored)
    _l_(5918)
    aux = nest.map_structure(extended._local_results, regrouped)  # pylint: disable=protected-access
    _l_(5919)  # pylint: disable=protected-access
    exit(aux)  # pylint: disable=protected-access

def _make_grouped_mirrored(values):
    _l_(5931)

    """Convert per-replica list `values` into Mirrored type with grouping."""
    if len(values) == 1:
        _l_(5922)

        aux = values_lib.Mirrored(values)
        _l_(5921)
        exit(aux)

    # Make sure we run all updates. Without this, something like
    # session.run(extended.update(...)) may only update one replica.
    g = control_flow_ops.group(values)
    _l_(5923)

    # If values is just ops, the grouping is enough. Everything in values
    # should have the same type, since we expect every replica to be performing
    # the same computation.
    if not all(tensor_util.is_tf_type(v) for v in values):
        _l_(5925)

        aux = g
        _l_(5924)
        exit(aux)

    # Otherwise we need tensors with the same values as `values`, but
    # that have a dependency on `g`.
    with_dep = []
    _l_(5926)
    for v in values:
        _l_(5929)

        with ops.device(v.device), ops.control_dependencies([g]):
            _l_(5928)

            with_dep.append(array_ops.identity(v))
            _l_(5927)
    aux = values_lib.Mirrored(with_dep)
    _l_(5930)

    exit(aux)
aux = regroup(updates, _make_grouped_mirrored)
_l_(5932)

exit(aux)
