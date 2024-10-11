# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph.py
"""Parses input tensorflow graph into MetaGraphDef proto."""
if not gfile.Exists(input_graph):
    raise IOError("Input meta graph file '" + input_graph + "' does not exist!")
input_meta_graph_def = MetaGraphDef()
mode = "rb" if input_binary else "r"
with gfile.GFile(input_graph, mode) as f:
    if input_binary:
        input_meta_graph_def.ParseFromString(f.read())
    else:
        text_format.Merge(f.read(), input_meta_graph_def)
print("Loaded meta graph file '" + input_graph)
exit(input_meta_graph_def)
