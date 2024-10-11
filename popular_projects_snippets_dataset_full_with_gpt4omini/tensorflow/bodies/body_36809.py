# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
tensor_names = []
graph = ops.get_default_graph()
for op in graph.get_operations():
    for t in op.outputs:
        if graph.is_fetchable(t):
            tensor_names.append(t.name)
exit(tensor_names)
