import timeit # pragma: no cover

num_ops = 5 # pragma: no cover
num_iters = 100 # pragma: no cover
func_graph = type('MockFuncGraph', (object,), {'FuncGraph': lambda name: type('MockGraph', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, exc_type, exc_val, exc_tb: None, 'as_default': lambda self: self})()}) # pragma: no cover
resource_variable_ops = type('MockResourceVariableOps', (object,), {'var_handle_op': lambda dtype, shape: 'mock_handle', 'assign_variable_op': lambda handle, value: None}) # pragma: no cover
gen_resource_variable_ops = type('MockGenResourceVariableOps', (object,), {'read_variable_op': lambda handle, dtype: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
from l3.Runtime import _l_
def add_op_to_graph(num_ops):
    _l_(17560)

    with func_graph.FuncGraph("resource").as_default():
        _l_(17559)

        handle = resource_variable_ops.var_handle_op(
            dtype=dtypes.int32, shape=[])
        _l_(17555)
        resource_variable_ops.assign_variable_op(
            handle, constant_op.constant(1, dtype=dtypes.int32))
        _l_(17556)
        for _ in range(num_ops):
            _l_(17558)

            gen_resource_variable_ops.read_variable_op(handle, dtype=dtypes.int32)
            _l_(17557)

runtimes = timeit.repeat(
    lambda: add_op_to_graph(num_ops), repeat=10, number=num_iters)
_l_(17561)
aux = min(runtimes) / num_iters
_l_(17562)
exit(aux)
