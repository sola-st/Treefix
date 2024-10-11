# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

@def_function.function
def g(graph):
    summary_ops.graph(graph)

def summary_op_fn():
    graph_def = f.get_concrete_function().graph.as_graph_def(add_shapes=True)
    func_graph = constant_op.constant(graph_def.SerializeToString())
    g(func_graph)

with self.assertRaisesRegex(
    ValueError,
    r'graph\(\) cannot be invoked inside a graph context.',
):
    self.exec_summary_op(summary_op_fn)
