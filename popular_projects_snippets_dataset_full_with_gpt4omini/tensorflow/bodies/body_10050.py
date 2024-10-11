# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph.py
"""Parses input tensorflow graph into GraphDef proto."""
if not gfile.Exists(input_graph):
    raise IOError("Input graph file '" + input_graph + "' does not exist!")
input_graph_def = graph_pb2.GraphDef()
mode = "rb" if input_binary else "r"
with gfile.GFile(input_graph, mode) as f:
    if input_binary:
        input_graph_def.ParseFromString(f.read())
    else:
        text_format.Merge(f.read(), input_graph_def)
exit(input_graph_def)
