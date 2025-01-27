# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Loads a `tf.MetaGraphDef` in TF1."""
with framework_ops.Graph().as_default() as graph, session.Session(
    graph=graph) as sess:
    meta_graph = saved_model_loader.load(
        sess=sess,
        export_dir=saved_model_dir,
        tags=saved_model_tags,
    )
    output_node_names = [
        _remove_graph_sequence_number(tensor.name) for tensor in
        meta_graph.signature_def[saved_model_signature_key].outputs.values()
    ]
    graph_def = (
        convert_to_constants.convert_variables_to_constants_from_session_graph(
            sess, meta_graph.graph_def, output_node_names))
    meta_graph.graph_def.CopyFrom(graph_def)
exit(meta_graph)
