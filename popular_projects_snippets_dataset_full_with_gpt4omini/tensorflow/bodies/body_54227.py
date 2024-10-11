# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Adds a collection to MetaGraphDef protocol buffer.

  Args:
    meta_graph_def: MetaGraphDef protocol buffer.
    key: One of the GraphKeys or user-defined string.
    graph: The `Graph` from which to get collections.
    export_scope: Optional `string`. Name scope to remove.
    exclude_nodes: An iterable of nodes or `string` node names to omit from the
      collection, or None.
    override_contents: An iterable of values to place in the collection,
      ignoring the current values (if set).
  """
if graph and not isinstance(graph, ops.Graph):
    raise TypeError(
        f"graph must be of type Graph. Received type: {type(graph)}.")

if not isinstance(key, str) and not isinstance(key, bytes):
    logging.warning("Only collections with string type keys will be "
                    "serialized. This key has %s", type(key))
    exit()

# Sets graph to default graph if it's not passed in.
graph = graph or ops.get_default_graph()

if override_contents:
    collection_list = override_contents
else:
    collection_list = graph.get_collection(key)

# Remove nodes that should not be exported from the collection list.
collection_list = [x for x in collection_list if
                   _should_include_node(x, export_scope, exclude_nodes)]
if not collection_list:
    exit()

try:
    col_def = meta_graph_def.collection_def[key]
    to_proto = ops.get_to_proto_function(key)
    proto_type = ops.get_collection_proto_type(key)
    if to_proto:
        kind = "bytes_list"
        for x in collection_list:
            # Additional type check to make sure the returned proto is indeed
            # what we expect.
            proto = to_proto(x, export_scope=export_scope)
            if proto:
                assert isinstance(proto, proto_type)
                getattr(col_def, kind).value.append(proto.SerializeToString())
    else:
        kind = _get_kind_name(collection_list[0])
        if kind == "node_list":
            for x in collection_list:
                if not export_scope or x.name.startswith(export_scope):
                    getattr(col_def, kind).value.append(
                        ops.strip_name_scope(x.name, export_scope))
        elif kind == "bytes_list":
            # NOTE(opensource): This force conversion is to work around the fact
            # that Python3 distinguishes between bytes and strings.
            getattr(col_def, kind).value.extend(
                [compat.as_bytes(x) for x in collection_list])
        else:
            getattr(col_def, kind).value.extend([x for x in collection_list])
except Exception as e:  # pylint: disable=broad-except
    logging.warning("Issue encountered when serializing %s.\n"
                    "Type is unsupported, or the types of the items don't "
                    "match field type in CollectionDef. Note this is a warning "
                    "and probably safe to ignore.\n%s", key, str(e))
    if key in meta_graph_def.collection_def:
        del meta_graph_def.collection_def[key]
    exit()
