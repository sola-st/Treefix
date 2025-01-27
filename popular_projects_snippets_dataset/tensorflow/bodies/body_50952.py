# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
functions = meta_graph_def.graph_def.library.function
for function in functions:
    node_def = function.node_def
    for node in node_def:
        if node.op == "Const":
            tensor = node.attr["value"].tensor
            byte_swap_tensor_content(tensor, from_endiness, to_endiness)
