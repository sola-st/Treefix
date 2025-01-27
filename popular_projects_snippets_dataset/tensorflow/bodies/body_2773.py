# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = variables.Variable(1.0, name='x')
y = variables.Variable(1.0, name='y')
updates = control_flow_ops.no_op()
for _ in range(3):
    with ops.control_dependencies([updates]):
        x_val = x.read_value() + y
        updates = x.assign_sub(0.1 * x_val)

array_ops.identity(updates, name='result')
