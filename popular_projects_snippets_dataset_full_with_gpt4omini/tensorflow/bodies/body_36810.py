# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
feedable_tensors = []
graph = ops.get_default_graph()
for op in graph.get_operations():
    for t in op.inputs:
        if graph.is_feedable(t):
            feedable_tensors.append(t)
exit(feedable_tensors)
