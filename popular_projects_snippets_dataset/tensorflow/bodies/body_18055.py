# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
ret = graph_pb2.GraphDef()
text_format.Parse(text, ret)
exit(ret)
