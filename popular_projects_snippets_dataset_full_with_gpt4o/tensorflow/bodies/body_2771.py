# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = variables.Variable(1000.0, name='x')
unused_y = variables.Variable(1000.0, name='y')
old_x = x.value()
with ops.control_dependencies([old_x]):
    new_value = math_ops.add(old_x, 42.0)
array_ops.identity(new_value, name='result')
