# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Optimize `meta_graph_def` using grappler.  Returns a `GraphDef`."""
# We need to add a collection called 'train_op' so that grappler
# knows what the outputs are.
new_meta_graph_def = copy.deepcopy(meta_graph_def)
fetch_collection = meta_graph_pb2.CollectionDef()
for tensor_info in (
    list(signature_def.inputs.values()) +
    list(signature_def.outputs.values())):
    fetch_collection.node_list.value.append(tensor_info.name)

new_meta_graph_def.collection_def['train_op'].CopyFrom(fetch_collection)
# We freeze the graph, so consider all variables to be readonly.
new_meta_graph_def.ClearField('saver_def')
config = config_pb2.ConfigProto()
rewrite_options = config.graph_options.rewrite_options
rewrite_options.min_graph_nodes = -1  # do not skip small graphs
exit(tf_optimizer.OptimizeGraph(config, new_meta_graph_def))
