group = None # pragma: no cover
def regroup(updates, mirrored): return updates # pragma: no cover
nest = type('Mock', (object,), {'map_structure': lambda fn, struct: struct})() # pragma: no cover
extended = type('Mock', (object,), {'_local_results': lambda: []})() # pragma: no cover
control_flow_ops = type('Mock', (object,), {'group': lambda values: values})() # pragma: no cover
ops = type('Mock', (object,), {'device': lambda v: None, 'control_dependencies': lambda deps: deps})() # pragma: no cover
array_ops = type('Mock', (object,), {'identity': lambda v: v})() # pragma: no cover
tensor_util = type('Mock', (object,), {'is_tf_type': lambda v: isinstance(v, tf.Tensor)})() # pragma: no cover

group = False # pragma: no cover
def regroup(updates, make_grouped): return updates # pragma: no cover
class MockValuesLib:  # pragma: no cover
    class Mirrored:  # pragma: no cover
        def __init__(self, values): # pragma: no cover
            self.values = values # pragma: no cover
values_lib = MockValuesLib() # pragma: no cover
class MockNest:  # pragma: no cover
    @staticmethod # pragma: no cover
    def map_structure(fn, struct): return [fn(item) for item in struct] # pragma: no cover
nest = MockNest() # pragma: no cover
class MockExtended:  # pragma: no cover
    @staticmethod # pragma: no cover
    def _local_results(): return 'local_results_placeholder' # pragma: no cover
extended = MockExtended() # pragma: no cover
class MockControlFlowOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def group(values): return values # pragma: no cover
control_flow_ops = MockControlFlowOps() # pragma: no cover
class MockOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def device(device_name): return device_name # pragma: no cover
    @staticmethod # pragma: no cover
    def control_dependencies(control_inputs): return control_inputs # pragma: no cover
ops = MockOps() # pragma: no cover
class MockArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def identity(x): return x # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
class MockTensorUtil:  # pragma: no cover
    @staticmethod # pragma: no cover
    def is_tf_type(x): return isinstance(x, (int, float, tf.Tensor)) # pragma: no cover
tensor_util = MockTensorUtil() # pragma: no cover

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
