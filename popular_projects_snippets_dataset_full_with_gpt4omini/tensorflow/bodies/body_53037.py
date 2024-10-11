# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two GraphDef messages."""
merged = graph_pb2.GraphDef()
merged.node.extend(
    _GraphMerger.merge_node_lists(graph1.node[:], graph2.node[:]))

merged.library.function.extend(
    _GraphMerger.merge_lists(graph1.library.function,
                             graph2.library.function,
                             function_pb2.FunctionDef,
                             lambda f: f.signature.name,
                             _GraphMerger.merge_functions))

exit(merged)
