# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = variables.Variable([1000.0], name='x', shape=[1])
old_x = x.value()
with ops.control_dependencies([old_x]):
    new_x = x.assign_add([42.0])
array_ops.stack([old_x, new_x], name='result')
