from unittest.mock import Mock # pragma: no cover

group = False # pragma: no cover
regroup = Mock(return_value=['regrouped_value']) # pragma: no cover
values_lib = Mock() # pragma: no cover
values_lib.Mirrored = Mock(side_effect=lambda x: f'Mirrored({x})') # pragma: no cover
nest = Mock() # pragma: no cover
nest.map_structure = Mock(side_effect=lambda func, *args, **kwargs: 'map_structure_result') # pragma: no cover
extended = Mock() # pragma: no cover
extended._local_results = Mock(side_effect=lambda grp: 'local_results') # pragma: no cover
control_flow_ops = Mock() # pragma: no cover
control_flow_ops.group = Mock(return_value='group_dependency') # pragma: no cover
ops = Mock() # pragma: no cover
ops.device.side_effect = lambda device: tf.device(device) # pragma: no cover
ops.control_dependencies.side_effect = lambda deps: tf.control_dependencies(deps) # pragma: no cover
array_ops = Mock() # pragma: no cover
tensor_util = Mock() # pragma: no cover
tensor_util.is_tf_type = Mock(side_effect=lambda v: isinstance(v, tf.Tensor)) # pragma: no cover

group = False # pragma: no cover
def regroup(updates, Mirrored): return Mirrored(updates) # pragma: no cover
values_lib = type('Mock', (object,), {'Mirrored': lambda x: x}) # pragma: no cover
nest = type('Mock', (object,), {'map_structure': lambda func, data: list(map(func, data))}) # pragma: no cover
extended = type('Mock', (object,), {'_local_results': lambda x: x}) # pragma: no cover

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
