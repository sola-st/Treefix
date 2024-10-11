group = False # pragma: no cover
def regroup(updates, values): return updates # pragma: no cover
values_lib = type('MockValuesLib', (object,), {'Mirrored': lambda self, x: x})() # pragma: no cover
nest = type('MockNest', (object,), {'map_structure': lambda self, func, struct: [func(v) for v in struct]})() # pragma: no cover
extended = type('MockExtended', (object,), {'_local_results': lambda self, x: x})() # pragma: no cover
control_flow_ops = type('MockControlFlowOps', (object,), {'group': lambda self, x: x})() # pragma: no cover
ops = type('MockOps', (object,), {'device': lambda self, v: None, 'control_dependencies': lambda self, deps: deps})() # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'identity': lambda self, v: v})() # pragma: no cover
tensor_util = type('MockTensorUtil', (object,), {'is_tf_type': lambda self, v: True})() # pragma: no cover

group = False # pragma: no cover
def regroup(updates, grouped_mirrored): return updates # pragma: no cover
values_lib = type('MockValuesLib', (object,), {'Mirrored': lambda self, x: x})() # pragma: no cover
nest = type('MockNest', (object,), {'map_structure': lambda func, structure: [func(x) for x in structure]})() # pragma: no cover
extended = type('MockExtended', (object,), {'_local_results': []})() # pragma: no cover
control_flow_ops = type('MockControlFlowOps', (object,), {'group': lambda x: x})() # pragma: no cover
ops = type('MockOps', (object,), {'device': lambda x: None, 'control_dependencies': lambda xs: xs})() # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'identity': lambda x: x})() # pragma: no cover
tensor_util = type('MockTensorUtil', (object,), {'is_tf_type': lambda x: True})() # pragma: no cover

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
