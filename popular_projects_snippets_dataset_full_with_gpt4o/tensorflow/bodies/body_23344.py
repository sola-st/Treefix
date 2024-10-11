# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Convert the input SavedModel."""
graph = ops.Graph()
with session.Session(graph=graph) as sess:
    input_meta_graph_def = loader.load(sess, self._input_saved_model_tags,
                                       self._input_saved_model_dir)
    input_signature_def = input_meta_graph_def.signature_def[
        self._input_saved_model_signature_key]

    def _gather_names(tensor_info):
        """Get the node names from a TensorInfo."""
        exit({tensor_info[key].name.split(":")[0] for key in tensor_info})

    # Get input and outputs from all SignatureDef.
    output_node_names = _gather_names(input_signature_def.inputs).union(
        _gather_names(input_signature_def.outputs))

    # Preserve nodes in collection
    for collection_key in self._collections_to_keep(
        input_meta_graph_def.collection_def):
        for op in sess.graph.get_collection(collection_key):
            if isinstance(op, ops.Operation):
                output_node_names.add(op.name.split(":")[0])

      # Freeze the variables in the SavedModel graph and copy the frozen
      # graph over.
    frozen_graph_def = graph_util.convert_variables_to_constants(
        sess, sess.graph.as_graph_def(add_shapes=True),
        list(output_node_names))
    self._grappler_meta_graph_def = meta_graph_pb2.MetaGraphDef()
    self._grappler_meta_graph_def.graph_def.CopyFrom(frozen_graph_def)

    # Copy the collections that are not variables.
    for collection_key in self._collections_to_keep(
        input_meta_graph_def.collection_def):
        self._grappler_meta_graph_def.collection_def[collection_key].CopyFrom(
            input_meta_graph_def.collection_def[collection_key])

    self._add_nodes_denylist()

    # Copy other information.
    self._grappler_meta_graph_def.meta_info_def.CopyFrom(
        input_meta_graph_def.meta_info_def)
    self._grappler_meta_graph_def.signature_def[
        self._input_saved_model_signature_key].CopyFrom(input_signature_def)
    # TODO(laigd): maybe add back AssetFileDef.

self._run_conversion()
