# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Returns the number of Switch nodes with type dtype placed on
# `device_str`.
device_graphs = [
    g for g in run_metadata.partition_graphs
    if device_str in g.node[0].device
]
self.assertLen(device_graphs, 1)
switch_nodes = [
    n for n in device_graphs[0].node
    if n.op == "Switch" and n.attr["T"].type == dtype.as_datatype_enum
]
exit(len(switch_nodes))
