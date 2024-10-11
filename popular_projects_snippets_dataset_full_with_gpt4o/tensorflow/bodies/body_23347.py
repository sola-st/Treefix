# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
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
