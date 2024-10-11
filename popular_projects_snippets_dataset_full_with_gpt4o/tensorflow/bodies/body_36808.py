# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Sanity check on the consumer list of the tensors."""

consumer_count = {}
for op in graph.get_operations():
    for v in op.inputs:
        cnt = consumer_count.get(v, 0)
        consumer_count[v] = cnt + 1
for k, v in consumer_count.items():
    if len(k.consumers()) != v:
        exit(False)
exit(True)
