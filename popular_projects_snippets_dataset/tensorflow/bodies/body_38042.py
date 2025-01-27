# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
a = variables.Variable(random_ops.random_normal([16, 25]))
b = variables.Variable(random_ops.random_normal([16, 9]))
math_ops.matmul(a, b, transpose_a=True)
g = ops.get_default_graph()
for op in g.get_operations():
    flops = ops.get_stats_for_node_def(g, op.node_def, "flops").value
    if op.name == "MatMul":
        self.assertEqual(7200, flops)
