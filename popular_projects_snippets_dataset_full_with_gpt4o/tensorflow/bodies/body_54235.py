# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Returns `MetaGraphDef` proto. Optionally writes it to filename.

  This function exports the graph, saver, and collection objects into
  `MetaGraphDef` protocol buffer with the intention of it being imported
  at a later time or location to restart training, run inference, or be
  a subgraph.

  Args:
    filename: Optional filename including the path for writing the
      generated `MetaGraphDef` protocol buffer.
    graph_def: `GraphDef` protocol buffer.
    graph: The `Graph` to export. If `None`, use the default graph.
    export_scope: Optional `string`. Name scope under which to extract
      the subgraph. The scope name will be stripped from the node definitions
      for easy import later into new name scopes. If `None`, the whole graph
      is exported.
    as_text: If `True`, writes the `MetaGraphDef` as an ASCII proto.
    unbound_inputs_col_name: Optional `string`. If provided, a string collection
      with the given name will be added to the returned `MetaGraphDef`,
      containing the names of tensors that must be remapped when importing the
      `MetaGraphDef`.
    clear_devices: Boolean which controls whether to clear device information
      before exporting the graph.
    saver_def: `SaverDef` protocol buffer.
    clear_extraneous_savers: Remove any Saver-related information from the
        graph (both Save/Restore ops and SaverDefs) that are not associated
        with the provided SaverDef.
    strip_default_attrs: Set to true if default valued attributes must be
      removed while exporting the GraphDef.
    save_debug_info: If `True`, save the GraphDebugInfo to a separate file,
      which in the same directory of filename and with `_debug` added before the
      file extension.
    **kwargs: Optional keyed arguments, including meta_info_def and
        collection_list.

  Returns:
    A `MetaGraphDef` proto and dictionary of `Variables` in the exported
    name scope.

  Raises:
    ValueError: When the `GraphDef` is larger than 2GB.
    ValueError: When executing in Eager mode and either `graph_def` or `graph`
      is undefined.
  """
if context.executing_eagerly() and not (graph_def is not None and
                                        graph is not None):
    raise ValueError("Exporting/importing meta graphs is not supported when "
                     "Eager Execution is enabled.")
graph = graph or ops.get_default_graph()

exclude_nodes = None
unbound_inputs = []
if export_scope or clear_extraneous_savers or clear_devices:
    if graph_def:
        new_graph_def = graph_pb2.GraphDef()
        new_graph_def.versions.CopyFrom(graph_def.versions)
        new_graph_def.library.CopyFrom(graph_def.library)

        if clear_extraneous_savers:
            exclude_nodes = _find_extraneous_saver_nodes(graph_def, saver_def)

        for node_def in graph_def.node:
            if _should_include_node(node_def.name, export_scope, exclude_nodes):
                new_node_def = _node_def(node_def, export_scope, unbound_inputs,
                                         clear_devices=clear_devices)
                new_graph_def.node.extend([new_node_def])
        graph_def = new_graph_def
    else:
        # Only do this complicated work if we want to remove a name scope.
        graph_def = graph_pb2.GraphDef()
        # pylint: disable=protected-access
        graph_def.versions.CopyFrom(graph.graph_def_versions)
        bytesize = 0

        if clear_extraneous_savers:
            exclude_nodes = _find_extraneous_saver_nodes(graph.as_graph_def(),
                                                         saver_def)

        for key in sorted(graph._nodes_by_id):
            if _should_include_node(graph._nodes_by_id[key].name,
                                    export_scope,
                                    exclude_nodes):
                value = graph._nodes_by_id[key]
                # pylint: enable=protected-access
                node_def = _node_def(value.node_def, export_scope, unbound_inputs,
                                     clear_devices=clear_devices)
                graph_def.node.extend([node_def])
                if value.outputs:
                    assert "_output_shapes" not in graph_def.node[-1].attr
                    graph_def.node[-1].attr["_output_shapes"].list.shape.extend([
                        output.get_shape().as_proto() for output in value.outputs])
                bytesize += value.node_def.ByteSize()
                if bytesize >= (1 << 31) or bytesize < 0:
                    raise ValueError(
                        "GraphDef cannot be larger than 2GB. "
                        f"Received size: {bytesize}.")

        graph._copy_functions_to_graph_def(graph_def, bytesize)  # pylint: disable=protected-access

    # It's possible that not all the inputs are in the export_scope.
    # If we would like such information included in the exported meta_graph,
    # add them to a special unbound_inputs collection.
    if unbound_inputs_col_name:
        # Clears the unbound_inputs collections.
        graph.clear_collection(unbound_inputs_col_name)
        for k in unbound_inputs:
            graph.add_to_collection(unbound_inputs_col_name, k)

var_list = {}
variables = graph.get_collection(ops.GraphKeys.GLOBAL_VARIABLES,
                                 scope=export_scope)
for v in variables:
    if _should_include_node(v, export_scope, exclude_nodes):
        var_list[ops.strip_name_scope(v.name, export_scope)] = v

scoped_meta_graph_def = create_meta_graph_def(
    graph_def=graph_def,
    graph=graph,
    export_scope=export_scope,
    exclude_nodes=exclude_nodes,
    clear_extraneous_savers=clear_extraneous_savers,
    saver_def=saver_def,
    strip_default_attrs=strip_default_attrs,
    **kwargs)

if filename:
    graph_io.write_graph(
        scoped_meta_graph_def,
        os.path.dirname(filename),
        os.path.basename(filename),
        as_text=as_text)
    if save_debug_info:
        name, _ = os.path.splitext(filename)
        debug_filename = "{name}{ext}".format(name=name, ext=".debug")

        # Gets the operation from the graph by the name. Excludes variable nodes,
        # so only the nodes in the frozen models are included.
        # TODO(liufengdb): fix this for functions.
        ops_to_export = []
        for node in scoped_meta_graph_def.graph_def.node:
            scoped_op_name = ops.prepend_name_scope(node.name, export_scope)
            ops_to_export.append(("", graph.get_operation_by_name(scoped_op_name)))

        graph_debug_info = error_interpolation.create_graph_debug_info_def(
            ops_to_export)

        graph_io.write_graph(
            graph_debug_info,
            os.path.dirname(debug_filename),
            os.path.basename(debug_filename),
            as_text=as_text)

exit((scoped_meta_graph_def, var_list))
