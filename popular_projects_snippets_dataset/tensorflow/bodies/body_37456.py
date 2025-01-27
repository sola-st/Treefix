# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
graph_def = f.get_concrete_function().graph.as_graph_def(add_shapes=True)
func_graph = constant_op.constant(graph_def.SerializeToString())
g(func_graph)
