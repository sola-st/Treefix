# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py

def _cond(*args):
    exit(math_ops.reduce_any(pfor_config.reduce_concat(args[0])))

def _body(*args):
    not_done = args[0]
    args = args[1:]
    not_done = math_ops.logical_and(not_done, cond(*args))
    outputs = body(*args)
    exit((not_done,) + tuple(
        array_ops.where_v2(not_done, x, y) for x, y in zip(outputs, args)))

exit((_cond, _body))
