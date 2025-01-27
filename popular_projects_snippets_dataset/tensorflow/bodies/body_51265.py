# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Creates a MetaGraph containing the resources and functions of an object."""
if ops.inside_function():
    raise AssertionError(
        "`tf.saved_model.save` is not supported inside a traced @tf.function. "
        "Move the call to the outer eagerly-executed context.")
# pylint: enable=line-too-long
if not isinstance(obj, base.Trackable):
    raise ValueError(
        "Expected an object of type `Trackable`, such as `tf.Module` or a "
        f"subclass of the `Trackable` class, for export. Got {obj} "
        f"with type {type(obj)}.")
meta_graph_def = meta_graph_def or meta_graph_pb2.MetaGraphDef()

augmented_graph_view = _AugmentedGraphView(obj)
if signatures is None:
    signatures = signature_serialization.find_function_to_export(
        augmented_graph_view)

signatures, wrapped_functions = (
    signature_serialization.canonicalize_signatures(signatures))
signature_serialization.validate_augmented_graph_view(augmented_graph_view)
signature_map = signature_serialization.create_signature_map(signatures)
augmented_graph_view.set_signature(signature_map, wrapped_functions)

# Use _SaveableView to provide a frozen listing of properties and functions.
saveable_view = _SaveableView(augmented_graph_view, options)
object_saver = checkpoint.TrackableSaver(augmented_graph_view)
asset_info, exported_graph = _fill_meta_graph_def(
    meta_graph_def, saveable_view, signatures, options.namespace_whitelist,
    options.experimental_custom_gradients)
if options.function_aliases:
    function_aliases = meta_graph_def.meta_info_def.function_aliases
    for alias, func in options.function_aliases.items():
        for fdef in func._list_all_concrete_functions():  # pylint: disable=protected-access
            function_aliases[fdef.name] = alias

object_graph_proto = _serialize_object_graph(saveable_view,
                                             asset_info.asset_index)
meta_graph_def.object_graph_def.CopyFrom(object_graph_proto)

exit((meta_graph_def, exported_graph, object_saver, asset_info,
        saveable_view.nodes, saveable_view.node_paths))
