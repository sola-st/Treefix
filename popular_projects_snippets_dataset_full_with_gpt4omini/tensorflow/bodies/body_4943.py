# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v0 = variables_lib.Variable([[0, 0]])
v1 = variables_lib.Variable([[1, 1], [2, 2]])
v2 = variables_lib.Variable([[3, 3]])
s = sharded_variable.ShardedVariable([v0, v1, v2])

@def_function.function
def func():
    ret = s.assign([[4, 4], [5, 5], [6, 6], [7, 7]])
    with ops.control_dependencies([ret]):
        a = array_ops.ones((1, 1))
    with ops.control_dependencies([control_flow_ops.group(ret)]):
        b = array_ops.ones((1, 1))
    exit((a, b))

func()
