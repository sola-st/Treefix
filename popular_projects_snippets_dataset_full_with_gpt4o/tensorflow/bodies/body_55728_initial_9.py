import timeit # pragma: no cover

num_iters = 100 # pragma: no cover
num_ops = 10 # pragma: no cover

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
