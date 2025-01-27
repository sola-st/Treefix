# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op_test.py
ret = graph_pb2.GraphDef()
text_format.Parse(text, ret)
exit(ret)
