# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
meta_graph = saved_model_proto.meta_graphs[0]
self._asset_file_def = meta_graph.asset_file_def
self._operation_attributes = {
    node.name: node.attr for node in meta_graph.graph_def.node}
self._proto = object_graph_proto
self._export_dir = export_dir
self._concrete_functions = (
    function_deserialization.load_function_def_library(
        library=meta_graph.graph_def.library,
        saved_object_graph=self._proto,
        wrapper_function=_WrapperFunction))
# Store a set of all concrete functions that have been set up with
# captures.
self._restored_concrete_functions = set()
self._checkpoint_options = ckpt_options
self._save_options = save_options

self._pretty_printer = checkpoint.ObjectGraphProtoPrettyPrinter(self._proto)

# Stores user-defined node_filters argument.
self._node_filters = filters
# Stores map of string paths to integers.
self._node_path_to_id = self._convert_node_paths_to_ints()
self._loaded_nodes = {}
if isinstance(filters, dict):
    # If node_filters is a dict, then the values may contain already created
    # trackable objects. In this case, create a dictionary mapping node IDs to
    # the already created nodes. This dict will be updated in
    # `_retrieve_all_filtered_nodes` with tracked children.
    for node_path, node in filters.items():
        if isinstance(node, tuple):
            self._loaded_nodes[self._node_path_to_id[node_path]] = node
        else:
            self._loaded_nodes[self._node_path_to_id[node_path]] = (node, setattr)

    # Get a list of all integer node ids to load, or None if all nodes should be
    # loaded. This list includes ids of child nodes.
self._filtered_nodes = self._retrieve_all_filtered_nodes()

# Order all nodes or filtered nodes using the dependencies.
self._ordered_node_ids = self._generate_ordered_node_ids()

self._load_all()

if not save_options.experimental_skip_checkpoint:
    self._restore_checkpoint()
for node in self._nodes:
    if isinstance(node, resource.CapturableResource):
        init_op = node._initialize()  # pylint: disable=protected-access
        if not context.executing_eagerly():
            ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, init_op)
