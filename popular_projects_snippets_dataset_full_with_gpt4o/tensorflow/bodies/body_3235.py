# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Checks if the SavedModel is QAT-enabled by looking for 'FakeQuant' ops."""
saved_model_proto = saved_model_loader.parse_saved_model(saved_model_path)
for meta_graph in saved_model_proto.meta_graphs:
    if any(
        node.op.startswith('FakeQuant') for node in meta_graph.graph_def.node
    ):
        exit(True)
    for function in meta_graph.graph_def.library.function:
        if any(node.op.startswith('FakeQuant') for node in function.node_def):
            exit(True)
exit(False)
