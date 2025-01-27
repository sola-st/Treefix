# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
# pylint: disable=line-too-long
"""Construct and returns a `MetaGraphDef` protocol buffer.

  Args:
    meta_info_def: `MetaInfoDef` protocol buffer.
    graph_def: `GraphDef` protocol buffer.
    saver_def: `SaverDef` protocol buffer.
    collection_list: List of string keys to collect.
    graph: The `Graph` to create `MetaGraphDef` out of.
    export_scope: Optional `string`. Name scope to remove.
    exclude_nodes: An iterable of nodes or `string` node names to omit from all
      collection, or None.
    clear_extraneous_savers: Remove any preexisting SaverDefs from the SAVERS
        collection.  Note this method does not alter the graph, so any
        extraneous Save/Restore ops should have been removed already, as needed.
    strip_default_attrs: Boolean. If `True`, default-valued attributes will be
        removed from the NodeDefs. For a detailed guide, see
        [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).

  Returns:
    MetaGraphDef protocol buffer.

  Raises:
    TypeError: If the arguments are not of the correct proto buffer type.
  """
# pylint: enable=line-too-long
# Type check.
if graph and not isinstance(graph, ops.Graph):
    raise TypeError(
        f"graph must be of type Graph. Received type: {type(graph)}.")
if meta_info_def and not isinstance(meta_info_def,
                                    meta_graph_pb2.MetaGraphDef.MetaInfoDef):
    raise TypeError(
        "meta_info_def must be of type MetaInfoDef. "
        f"Received type: {type(meta_info_def)}.")
if graph_def and not isinstance(graph_def, graph_pb2.GraphDef):
    raise TypeError(
        "graph_def must be of type GraphDef. "
        f"Received type: {type(graph_def)}.")
if saver_def and not isinstance(saver_def, saver_pb2.SaverDef):
    raise TypeError(
        f"saver_def must be of type SaverDef. "
        f"Received type: {type(saver_def)}.")

# Sets graph to default graph if it's not passed in.
graph = graph or ops.get_default_graph()

# Creates a MetaGraphDef proto.
meta_graph_def = meta_graph_pb2.MetaGraphDef()
# Adds meta_info_def.
if not meta_info_def:
    meta_info_def = meta_graph_pb2.MetaGraphDef.MetaInfoDef()

# Set the tf version strings to the current tf build.
meta_info_def.tensorflow_version = versions.__version__
meta_info_def.tensorflow_git_version = versions.__git_version__
meta_graph_def.meta_info_def.MergeFrom(meta_info_def)

# Adds graph_def or the default.
if not graph_def:
    meta_graph_def.graph_def.MergeFrom(graph.as_graph_def(add_shapes=True))
else:
    meta_graph_def.graph_def.MergeFrom(graph_def)

# Fills in meta_info_def.stripped_op_list using the ops from graph_def.
# pylint: disable=g-explicit-length-test
if len(meta_graph_def.meta_info_def.stripped_op_list.op) == 0:
    meta_graph_def.meta_info_def.stripped_op_list.MergeFrom(
        stripped_op_list_for_graph(meta_graph_def.graph_def))
# pylint: enable=g-explicit-length-test

# Strip default valued attributes in graph_def.
if strip_default_attrs:
    strip_graph_default_valued_attrs(meta_graph_def)

# Adds saver_def.
if saver_def:
    meta_graph_def.saver_def.MergeFrom(saver_def)

# Adds collection_list.
if collection_list is not None:
    clist = collection_list
else:
    clist = graph.get_all_collection_keys()

for ctype in clist:
    if clear_extraneous_savers and ctype == ops.GraphKeys.SAVERS:
        # Avoid importing Saver here
        from_proto = ops.get_from_proto_function(ctype)
        add_collection_def(meta_graph_def, ctype,
                           graph=graph,
                           export_scope=export_scope,
                           exclude_nodes=exclude_nodes,
                           override_contents=[from_proto(saver_def)])
    else:
        add_collection_def(meta_graph_def, ctype,
                           graph=graph,
                           export_scope=export_scope,
                           exclude_nodes=exclude_nodes)
exit(meta_graph_def)
