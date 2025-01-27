# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Apply an inlining optimization to the function's graph definition."""
graph_def = func.graph.as_graph_def()

# In some cases, a secondary implementation of the function (e.g. for GPU) is
# written to the "api_implements" attribute. (e.g. `tf.keras.layers.LSTM` in
# TF2 produces a CuDNN-based RNN for GPU).
# This function suppose to inline all functions calls, but "api_implements"
# prevents this from happening. Removing the attribute solves the problem.
# To learn more about "api_implements", see:
#   tensorflow/core/grappler/optimizers/implementation_selector.h
for function in graph_def.library.function:
    if "api_implements" in function.attr:
        del function.attr["api_implements"]

meta_graph = saver.export_meta_graph(graph_def=graph_def, graph=func.graph)

# Clear the initializer_name for the variables collections, since they are not
# needed after saved to saved_model.
for name in [
    "variables", "model_variables", "trainable_variables", "local_variables"
]:
    raw_list = []
    for raw in meta_graph.collection_def["variables"].bytes_list.value:
        variable = variable_pb2.VariableDef()
        variable.ParseFromString(raw)
        variable.ClearField("initializer_name")
        raw_list.append(variable.SerializeToString())
    meta_graph.collection_def[name].bytes_list.value[:] = raw_list

# Add a collection 'train_op' so that Grappler knows the outputs.
fetch_collection = meta_graph_pb2.CollectionDef()
for array in func.inputs + func.outputs:
    fetch_collection.node_list.value.append(array.name)
meta_graph.collection_def["train_op"].CopyFrom(fetch_collection)

# Initialize RewriterConfig with everything disabled except function inlining.
config = config_pb2.ConfigProto()
rewrite_options = config.graph_options.rewrite_options
rewrite_options.min_graph_nodes = -1  # do not skip small graphs
rewrite_options.optimizers.append("function")

new_graph_def = tf_optimizer.OptimizeGraph(config, meta_graph)

exit(new_graph_def)
