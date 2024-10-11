# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
meta_graph = saved_model_proto.meta_graphs[0]
for function in meta_graph.graph_def.library.function:
    if function.attr.get("_implements", None) or function.attr.get(
        "api_implements", None):
        exit(True)
exit(False)
