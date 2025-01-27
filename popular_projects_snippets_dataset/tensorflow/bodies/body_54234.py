# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Imports graph from `MetaGraphDef` and returns vars and return elements.

  This function takes a `MetaGraphDef` protocol buffer as input. If
  the argument is a file containing a `MetaGraphDef` protocol buffer ,
  it constructs a protocol buffer from the file content. The function
  then adds all the nodes from the `graph_def` field to the
  current graph, recreates the desired collections, and returns a dictionary of
  all the Variables imported into the name scope.

  In combination with `export_scoped_meta_graph()`, this function can be used to

  * Serialize a graph along with other Python objects such as `QueueRunner`,
    `Variable` into a `MetaGraphDef`.

  * Restart training from a saved graph and checkpoints.

  * Run inference from a saved graph and checkpoints.

  Args:
    meta_graph_or_file: `MetaGraphDef` protocol buffer or filename (including
      the path) containing a `MetaGraphDef`.
    clear_devices: Boolean which controls whether to clear device information
      from graph_def. Default false.
    graph: The `Graph` to import into. If `None`, use the default graph.
    import_scope: Optional `string`. Name scope into which to import the
      subgraph. If `None`, the graph is imported to the root name scope.
    input_map: A dictionary mapping input names (as strings) in `graph_def` to
      `Tensor` objects. The values of the named input tensors in the imported
      graph will be re-mapped to the respective `Tensor` values.
    unbound_inputs_col_name: Collection name for looking up unbound inputs.
    restore_collections_predicate: a predicate on collection names. A collection
      named c (i.e whose key is c) will be restored iff
      1) `restore_collections_predicate(c)` is True, and
      2) `c != unbound_inputs_col_name`.
    return_elements:  A list of strings containing operation names in the
      `MetaGraphDef` that will be returned as `Operation` objects; and/or
      tensor names in `MetaGraphDef` that will be returned as `Tensor` objects.

  Returns:
    A tuple of (
      dictionary of all the `Variables` imported into the name scope,
      list of `Operation` or `Tensor` objects from the `return_elements` list).

  Raises:
    ValueError: If the graph_def contains unbound inputs.

  """
if context.executing_eagerly():
    raise ValueError("Exporting/importing meta graphs is not supported when "
                     "eager execution is enabled.")
if isinstance(meta_graph_or_file, meta_graph_pb2.MetaGraphDef):
    meta_graph_def = meta_graph_or_file
else:
    meta_graph_def = read_meta_graph_file(meta_graph_or_file)

if unbound_inputs_col_name:
    for key, col_def in meta_graph_def.collection_def.items():
        if key == unbound_inputs_col_name:
            kind = col_def.WhichOneof("kind")
            field = getattr(col_def, kind)
            if field.value and (
                not input_map or
                sorted([compat.as_str(v) for v in field.value]) !=
                sorted(input_map)):
                raise ValueError("Graph contains unbound inputs: %s. Must "
                                 "provide these inputs through input_map." % ",".join(
                                     compat.as_str(v)
                                     for v in field.value
                                     if not input_map or v not in input_map))
            break

  # Sets graph to default graph if it's not passed in.
graph = graph or ops.get_default_graph()

# Gathers the list of nodes we are interested in.
with graph.as_default():
    producer_op_list = None
    if meta_graph_def.meta_info_def.HasField("stripped_op_list"):
        producer_op_list = meta_graph_def.meta_info_def.stripped_op_list
    input_graph_def = meta_graph_def.graph_def
    # Remove all the explicit device specifications for this node. This helps to
    # make the graph more portable.
    if clear_devices:
        for node in input_graph_def.node:
            node.device = ""

    scope_to_prepend_to_names = graph.unique_name(
        import_scope or "", mark_as_used=False)

    imported_return_elements = importer.import_graph_def(
        input_graph_def,
        name=(import_scope or scope_to_prepend_to_names),
        input_map=input_map,
        producer_op_list=producer_op_list,
        return_elements=return_elements)

    # TensorFlow versions before 1.9 (not inclusive) exported SavedModels
    # without a VariableDef.trainable field set.
    tf_version = meta_graph_def.meta_info_def.tensorflow_version
    if not tf_version:
        variables_have_trainable = True
    else:
        variables_have_trainable = (
            packaging_version.parse(tf_version) >= packaging_version.parse("1.9"))

    # Sort collections so we see TRAINABLE_VARIABLES first and can default these
    # variables to trainable if the value is not set in their VariableDef.
    sorted_collections = []
    if ops.GraphKeys.TRAINABLE_VARIABLES in meta_graph_def.collection_def:
        sorted_collections.append(
            (ops.GraphKeys.TRAINABLE_VARIABLES,
             meta_graph_def.collection_def[ops.GraphKeys.TRAINABLE_VARIABLES]))
    for key, value in sorted(meta_graph_def.collection_def.items()):
        if key != ops.GraphKeys.TRAINABLE_VARIABLES:
            sorted_collections.append((key, value))

    # Restores all the other collections.
    variable_objects = {}
    for key, col_def in sorted_collections:
        # Don't add unbound_inputs to the new graph.
        if key == unbound_inputs_col_name:
            continue
        if not restore_collections_predicate(key):
            continue

        kind = col_def.WhichOneof("kind")
        if kind is None:
            logging.error("Cannot identify data type for collection %s. Skipping.",
                          key)
            continue
        from_proto = ops.get_from_proto_function(key)

        # Temporary change to allow the TFMA evaluator to read metric variables
        # saved as a bytes list.
        # TODO(kathywu): Remove this hack once cl/248406059 has been submitted.
        if key == ops.GraphKeys.METRIC_VARIABLES:
            # Metric variables will use the same proto functions as GLOBAL_VARIABLES
            from_proto = ops.get_from_proto_function(ops.GraphKeys.GLOBAL_VARIABLES)
        if from_proto and kind == "bytes_list":
            proto_type = ops.get_collection_proto_type(key)
            if key in ops.GraphKeys._VARIABLE_COLLECTIONS:  # pylint: disable=protected-access
                for value in col_def.bytes_list.value:
                    variable = variable_objects.get(value, None)
                    if variable is None:
                        proto = proto_type()
                        proto.ParseFromString(value)
                        if not variables_have_trainable:
                            # If the VariableDef proto does not contain a "trainable"
                            # property because it was exported before that property was
                            # added, we default it to whether the variable is in the
                            # TRAINABLE_VARIABLES collection. We've sorted
                            # TRAINABLE_VARIABLES to be first, so trainable variables will
                            # be created from that collection.
                            proto.trainable = (key == ops.GraphKeys.TRAINABLE_VARIABLES)
                        variable = from_proto(
                            proto, import_scope=scope_to_prepend_to_names)
                        variable_objects[value] = variable
                    graph.add_to_collection(key, variable)
            else:
                for value in col_def.bytes_list.value:
                    proto = proto_type()
                    proto.ParseFromString(value)
                    graph.add_to_collection(
                        key, from_proto(
                            proto, import_scope=scope_to_prepend_to_names))
        else:
            field = getattr(col_def, kind)
            if key in _COMPAT_COLLECTION_LIST:
                logging.warning(
                    "The saved meta_graph is possibly from an older release:\n"
                    "'%s' collection should be of type 'byte_list', but instead "
                    "is of type '%s'.", key, kind)
            if kind == "node_list":
                for value in field.value:
                    col_op = graph.as_graph_element(
                        ops.prepend_name_scope(value, scope_to_prepend_to_names))
                    graph.add_to_collection(key, col_op)
            elif kind == "int64_list":
                # NOTE(opensource): This force conversion is to work around the fact
                # that Python2 distinguishes between int and long, while Python3 has
                # only int.
                for value in field.value:
                    graph.add_to_collection(key, int(value))
            else:
                for value in field.value:
                    graph.add_to_collection(
                        key, ops.prepend_name_scope(value, scope_to_prepend_to_names))

    var_list = {}
    variables = graph.get_collection(ops.GraphKeys.GLOBAL_VARIABLES,
                                     scope=scope_to_prepend_to_names)
    for v in variables:
        var_list[ops.strip_name_scope(v.name, scope_to_prepend_to_names)] = v

exit((var_list, imported_return_elements))
