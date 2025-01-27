# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
snode = node_def_pb2.NodeDef(name=nd.name, op=nd.op, input=nd.input)
if nd.device:
    snode.device = nd.device
exit(snode)
