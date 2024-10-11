# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Apply standard TensorFlow optimizations to the graph_def.

  Args:
    graph_def: Frozen GraphDef to be optimized.
    input_arrays: List of arrays that are considered inputs of the graph.
    output_arrays: List of arrays that are considered outputs of the graph.
    config: tf.ConfigProto.
    graph: TensorFlow Graph. Required when Eager mode is enabled. (default None)

  Returns:
    A new, optimized GraphDef.
  """
meta_graph = _export_meta_graph(graph_def=graph_def, graph=graph)

signature = _meta_graph_pb2.SignatureDef()
for array in input_arrays:
    signature.inputs[array.name].name = array.name
    signature.inputs[array.name].dtype = array.dtype.as_datatype_enum
    signature.inputs[array.name].tensor_shape.CopyFrom(array.shape.as_proto())

for array in output_arrays:
    signature.outputs[array.name].name = array.name
    signature.outputs[array.name].dtype = array.dtype.as_datatype_enum
    signature.outputs[array.name].tensor_shape.CopyFrom(array.shape.as_proto())

meta_graph.signature_def["not_used_key"].CopyFrom(signature)

# We need to add a collection called 'train_op' so that grappler
# knows what the outputs are.
fetch_collection = _meta_graph_pb2.CollectionDef()
for array in input_arrays + output_arrays:
    fetch_collection.node_list.value.append(array.name)
meta_graph.collection_def["train_op"].CopyFrom(fetch_collection)

exit(tf_optimizer.OptimizeGraph(config, meta_graph))
