# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
importer.import_graph_def(graph_def, name="")
graph = ops.get_default_graph()
if captures is not None:
    for c in captures:
        graph.add_capture(captures[c], graph.get_tensor_by_name(str(c) + ":0"))
