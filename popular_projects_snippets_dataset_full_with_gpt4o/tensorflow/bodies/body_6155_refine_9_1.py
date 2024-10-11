group = False # pragma: no cover
regroup = lambda updates, func: func(updates) # pragma: no cover
values_lib = type('ValuesLib', (object,), {'Mirrored': lambda x: x}) # pragma: no cover
nest = type('Nest', (object,), {'map_structure': lambda func, x: func(x)}) # pragma: no cover
extended = type('Extended', (object,), {'_local_results': lambda x: x}) # pragma: no cover
tensor_util = type('TensorUtil', (object,), {'is_tf_type': lambda x: isinstance(x, tf.Tensor)}) # pragma: no cover

group = False # pragma: no cover
def regroup(updates, mirrored_fn): return mirrored_fn(updates) # pragma: no cover
values_lib = type('ValuesLib', (object,), {'Mirrored': lambda x: x}) # pragma: no cover
nest = type('Nest', (object,), {'map_structure': lambda func, structure: [func(s) for s in structure]}) # pragma: no cover
extended = type('Extended', (object,), {'_local_results': lambda x: x}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
from l3.Runtime import _l_
"""Regroup for an update, with dependencies to ensure all updates execute."""
if not group:
    _l_(17883)

    regrouped = regroup(updates, values_lib.Mirrored)
    _l_(17881)
    aux = nest.map_structure(extended._local_results, regrouped)  # pylint: disable=protected-access
    _l_(17882)  # pylint: disable=protected-access
    exit(aux)  # pylint: disable=protected-access

def _make_grouped_mirrored(values):
    _l_(17894)

    """Convert per-replica list `values` into Mirrored type with grouping."""
    if len(values) == 1:
        _l_(17885)

        aux = values_lib.Mirrored(values)
        _l_(17884)
        exit(aux)

    # Make sure we run all updates. Without this, something like
    # session.run(extended.update(...)) may only update one replica.
    g = control_flow_ops.group(values)
    _l_(17886)

    # If values is just ops, the grouping is enough. Everything in values
    # should have the same type, since we expect every replica to be performing
    # the same computation.
    if not all(tensor_util.is_tf_type(v) for v in values):
        _l_(17888)

        aux = g
        _l_(17887)
        exit(aux)

    # Otherwise we need tensors with the same values as `values`, but
    # that have a dependency on `g`.
    with_dep = []
    _l_(17889)
    for v in values:
        _l_(17892)

        with ops.device(v.device), ops.control_dependencies([g]):
            _l_(17891)

            with_dep.append(array_ops.identity(v))
            _l_(17890)
    aux = values_lib.Mirrored(with_dep)
    _l_(17893)

    exit(aux)
aux = regroup(updates, _make_grouped_mirrored)
_l_(17895)

exit(aux)
