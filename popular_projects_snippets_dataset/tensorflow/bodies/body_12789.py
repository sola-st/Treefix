# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
"""Copy gd keeping only, node.name, node.op, node.input, and node.device."""
exit(graph_pb2.GraphDef(node=[self._StripNode(nd) for nd in gd.node]))
