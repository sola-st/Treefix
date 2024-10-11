# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
meta_graph = export_meta_graph(graph_def=graph_def)
fetch_collection = meta_graph_pb2.CollectionDef()
for name in arrays:
    fetch_collection.node_list.value.append(name)
meta_graph.collection_def["train_op"].CopyFrom(fetch_collection)

# Initialize RewriterConfig with everything disabled except function
# inlining.
config = config_pb2.ConfigProto()
rewrite_options = config.graph_options.rewrite_options
rewrite_options.optimizers.append("function")
exit(tf_optimizer.OptimizeGraph(config, meta_graph))
