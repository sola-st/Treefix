# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Save the converted graph as a SavedModel.

    Args:
      output_saved_model_dir: construct a SavedModel using the converted
        GraphDef and save it to the specified directory. This option only works
        when the input graph is loaded from a SavedModel, i.e. when
        input_saved_model_dir is specified and input_graph_def is None in
        __init__().

    Raises:
      ValueError: if the input to the converter is a GraphDef instead of a
      SavedModel.
    """
assert self._converted
if self._need_calibration:
    assert self._calibration_data_collected
if self._input_graph_def:
    raise ValueError(
        "Not able to save to a SavedModel since input is a GraphDef")

def _restore_collections(dest_graph, src_meta_graph_def, collection_keys):
    """Restores collections that we need to keep."""
    scope = ""
    for key in collection_keys:
        collection_def = src_meta_graph_def.collection_def[key]
        kind = collection_def.WhichOneof("kind")
        if kind is None:
            logging.error(
                "Cannot identify data type for collection %s. Skipping.", key)
            continue
        from_proto = ops.get_from_proto_function(key)
        if from_proto and kind == "bytes_list":
            proto_type = ops.get_collection_proto_type(key)
            # It is assumed that there are no Variables Keys in collections
            for value in collection_def.bytes_list.value:
                proto = proto_type()
                proto.ParseFromString(value)
                try:
                    new_value = from_proto(proto, import_scope=scope)
                except:
                    continue
                dest_graph.add_to_collection(key, new_value)
        else:
            field = getattr(collection_def, kind)
            if kind == "node_list":
                for value in field.value:
                    name = ops.prepend_name_scope(value, scope)
                    # Since the graph has been optimized, the node may no longer
                    # exists
                    try:
                        col_op = dest_graph.as_graph_element(name)
                    except (TypeError, ValueError, KeyError):
                        continue
                    dest_graph.add_to_collection(key, col_op)
            elif kind == "int64_list":
                # NOTE(opensource): This force conversion is to work around the
                # fact that Python2 distinguishes between int and long, while
                # Python3 has only int.
                for value in field.value:
                    dest_graph.add_to_collection(key, int(value))
            else:
                for value in field.value:
                    dest_graph.add_to_collection(key,
                                                 ops.prepend_name_scope(value, scope))

    # Write the transformed graphdef as SavedModel.
saved_model_builder = builder.SavedModelBuilder(output_saved_model_dir)
with ops.Graph().as_default():
    importer.import_graph_def(self._converted_graph_def, name="")
    _restore_collections(
        ops.get_default_graph(), self._grappler_meta_graph_def,
        self._collections_to_keep(
            self._grappler_meta_graph_def.collection_def))
    # We don't use any specific converter here.
    with session.Session() as sess:
        saved_model_builder.add_meta_graph_and_variables(
            sess,
            self._input_saved_model_tags,
            signature_def_map=self._grappler_meta_graph_def.signature_def)
    # Ignore other meta graphs from the input SavedModel.
saved_model_builder.save()
