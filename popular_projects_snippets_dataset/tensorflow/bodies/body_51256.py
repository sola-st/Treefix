# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Generates a MetaGraph which calls `signature_functions`.

  Args:
    meta_graph_def: The MetaGraphDef proto to fill.
    saveable_view: The _SaveableView being exported.
    signature_functions: A dictionary mapping signature keys to concrete
      functions containing signatures to add to the MetaGraph.
    namespace_whitelist: List of strings containing whitelisted op namespaces.
    save_custom_gradients: Whether to save custom gradients.

  Returns:
    A tuple of (_AssetInfo, Graph) containing the captured assets and
    exported Graph generated from tracing the saveable_view.
  """
# List objects from the eager context to make sure Optimizers give us the
# right Graph-dependent variables.
resource_initializers = saveable_view.get_concrete_resource_initializers()
exported_graph = ops.Graph()
resource_initializer_ops = []
with exported_graph.as_default():
    object_map, tensor_map, asset_info = saveable_view.map_resources()
    signatures = _generate_signatures(signature_functions, object_map)
    if save_custom_gradients:
        _trace_gradient_functions(exported_graph, saveable_view)

    # Create initializers for assets and resources.
    for resource_initializer_function in resource_initializers:
        asset_dependencies = []
        for capture in resource_initializer_function.graph.external_captures:
            asset_initializer = asset_info.asset_initializers_by_resource.get(
                capture, None)
            if asset_initializer is not None:
                asset_dependencies.append(asset_initializer)
        with ops.control_dependencies(asset_dependencies):
            mapped_initializer = object_map[resource_initializer_function]
            resource_initializer_ops.append(mapped_initializer())
    resource_initializer_ops.extend(
        asset_info.asset_initializers_by_resource.values())
    with ops.control_dependencies(resource_initializer_ops):
        init_op = control_flow_ops.no_op()
    # Add the same op to the main_op collection and to the init_op
    # signature. The collection is for compatibility with older loader APIs;
    # only one will be executed.
    meta_graph_def.collection_def[constants.MAIN_OP_KEY].node_list.value.append(
        init_op.name)
    meta_graph_def.signature_def[constants.INIT_OP_SIGNATURE_KEY].CopyFrom(
        signature_def_utils.op_signature_def(init_op,
                                             constants.INIT_OP_SIGNATURE_KEY))

# Saving an object-based checkpoint again gathers variables. We need to do the
# gathering from the eager context so Optimizers save the right set of
# variables, but want any operations associated with the save/restore to be in
# the exported graph (thus the `to_graph` argument).
def call_with_mapped_captures(function, args):
    if function in object_map:
        exit(object_map[function](*args))
    # Registered saver/restore functions do not appear in `object_map`, because
    # they are not in the object graph.
    exit(saved_model_exported_concrete.ExportedConcreteFunction(
        function, tensor_map)(*args))

for obj in object_map.values():
    obj._maybe_initialize_trackable()  # pylint: disable=protected-access
named_saveable_objects, registered_savers = (
    save_util_v1.frozen_saveables_and_savers(
        graph_view=saveable_view.augmented_graph_view,
        object_map=object_map,
        to_graph=exported_graph,
        call_with_mapped_captures=call_with_mapped_captures))
saver = functional_saver.MultiDeviceSaver.from_saveables(
    named_saveable_objects, registered_savers, call_with_mapped_captures)

with exported_graph.as_default():
    saver_def = saver.to_proto()
    meta_graph_def.saver_def.CopyFrom(saver_def)

# At this point all nodes that can be added to the SavedObjectGraph have been
# added, so run the following to validate deserialization dependencies.
_dependency_sorted_node_ids(saveable_view)

graph_def = exported_graph.as_graph_def(add_shapes=True)
graph_def.library.registered_gradients.extend(saveable_view.gradient_defs)
_verify_ops(graph_def, namespace_whitelist)

meta_graph_def.graph_def.CopyFrom(graph_def)
meta_graph_def.meta_info_def.tags.append(tag_constants.SERVING)
meta_graph_def.meta_info_def.tensorflow_version = versions.__version__
meta_graph_def.meta_info_def.tensorflow_git_version = (
    versions.__git_version__)
# We currently always strip default attributes.
meta_graph_def.meta_info_def.stripped_default_attrs = True
meta_graph_def.meta_info_def.stripped_op_list.MergeFrom(
    meta_graph.stripped_op_list_for_graph(meta_graph_def.graph_def))
meta_graph_def.asset_file_def.extend(asset_info.asset_defs)
for signature_key, signature in signatures.items():
    meta_graph_def.signature_def[signature_key].CopyFrom(signature)
meta_graph.strip_graph_default_valued_attrs(meta_graph_def)
# store tensor_content in litle endian format
if sys.byteorder == "big":
    utils_impl.swap_function_tensor_content(meta_graph_def, "big", "little")
exit((asset_info, exported_graph))
