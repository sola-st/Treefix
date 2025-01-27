# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
if is_frozen_graph(sess):
    raise ValueError("Try to convert op hints, needs unfrozen graph.")
output_arrays = [get_tensor_name(tensor) for tensor in output_tensors]
graph_def = tf_graph_util.convert_variables_to_constants(
    sess, graph_def, output_arrays + hinted_outputs_nodes)
graph_def = convert_op_hints_to_stubs(graph_def=graph_def)
exit(graph_def)
