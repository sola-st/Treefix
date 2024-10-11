# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Creates an object from the MetaGraph identified by `tags`."""
meta_graph_def = self.get_meta_graph_def_from_tags(tags)
load_shared_name_suffix = "_load_{}".format(ops.uid())
functions = function_deserialization.load_function_def_library(
    meta_graph_def.graph_def.library,
    load_shared_name_suffix=load_shared_name_suffix)
# Replace existing functions in the MetaGraphDef with renamed functions so
# we don't have duplicates or name collisions.
meta_graph_def.graph_def.library.Clear()
for function in functions.values():
    meta_graph_def.graph_def.library.function.add().CopyFrom(
        function.function_def)
# We've renamed functions and shared names. We need the same operation on
# the GraphDef itself for consistency.
for node_def in meta_graph_def.graph_def.node:
    function_deserialization.fix_node_def(node_def, functions,
                                          load_shared_name_suffix)

load_graph_returns = [None]
wrapped = wrap_function.wrap_function(
    functools.partial(self.load_graph, load_graph_returns, meta_graph_def),
    signature=[])
saver, = load_graph_returns
restore_from_saver = self._extract_saver_restore(wrapped, saver)
self.restore_variables(wrapped, restore_from_saver)
with wrapped.graph.as_default():
    init_op = loader_impl.get_init_op(
        meta_graph_def) or monitored_session.Scaffold.default_local_init_op()
    # Add a dummy Tensor we know we can fetch to add control dependencies to.
    init_anchor = constant_op.constant(0., name="dummy_fetch")

root = autotrackable.AutoTrackable()
if restore_from_saver is not None:
    root.restore = (
        lambda path: restore_from_saver(constant_op.constant(path)))
asset_feed_tensors = []
asset_paths = []
for tensor_name, value in loader_impl.get_asset_tensors(
    self._export_dir, meta_graph_def).items():
    asset_feed_tensors.append(wrapped.graph.as_graph_element(tensor_name))
    asset_paths.append(asset.Asset(value))
init_fn = wrapped.prune(
    feeds=asset_feed_tensors,
    fetches=[init_anchor, wrapped.graph.as_graph_element(init_op)])
initializer = _Initializer(init_fn, asset_paths)
# pylint: disable=protected-access
local_init_op, _ = initializer._initialize()
# pylint: enable=protected-access
with ops.init_scope():
    if not context.executing_eagerly():
        ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, local_init_op)
        for variable in wrapped.graph.get_collection_ref(
            ops.GraphKeys.LOCAL_VARIABLES):
            # pylint: disable=protected-access
            variable._initializer_op = local_init_op
            # pylint: enable=protected-access
root.initializer = initializer
root.asset_paths = asset_paths
signature_functions = self._extract_signatures(wrapped, meta_graph_def)

root.signatures = signature_serialization.create_signature_map(
    signature_functions)
root.variables = list(wrapped.graph.variables)
root.tensorflow_version = (
    meta_graph_def.meta_info_def.tensorflow_version)
root.tensorflow_git_version = (
    meta_graph_def.meta_info_def.tensorflow_git_version)
root.graph = wrapped.graph
root.prune = wrapped.prune
exit(root)
