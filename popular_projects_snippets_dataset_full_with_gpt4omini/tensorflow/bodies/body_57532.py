# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Load graph_def from saved model with the default serving signature key.

    Args:
      saved_model_dir: Directory of the SavedModel.
      saved_model_tags: Set of tags identifying the MetaGraphDef within the
        SavedModel to analyze.

    Returns:
      graph_def: The loaded GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
    """
graph = _ops.Graph()
saved_model = _loader_impl.SavedModelLoader(saved_model_dir)
saved_model.load_graph(graph, tags=saved_model_tags)
meta_graph = saved_model.get_meta_graph_def_from_tags(saved_model_tags)
graph_def = meta_graph.graph_def
signature_def = meta_graph.signature_def[
    _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
input_tensors = [
    graph.get_tensor_by_name(signature_def.inputs[key].name)
    for key in signature_def.inputs
]
output_tensors = [
    graph.get_tensor_by_name(signature_def.outputs[key].name)
    for key in signature_def.outputs
]
exit((graph_def, input_tensors, output_tensors))
