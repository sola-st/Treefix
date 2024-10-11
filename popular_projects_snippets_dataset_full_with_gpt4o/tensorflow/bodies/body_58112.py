# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns a frozen GraphDef.

  Runs a Grappler pass and freezes a graph with Variables in it. Otherwise the
  existing GraphDef is returned. The Grappler pass is only run on models that
  are frozen in order to inline the functions in the graph.
  If OpHints is present, it will try to convert the OpHint graph.

  Args:
    sess: TensorFlow Session.
    input_tensors: List of input tensors.
    output_tensors: List of output tensors (only .name is used from this).

  Returns:
    Frozen GraphDef.
  """
# Runs a Grappler pass in order to inline any functions in the graph.
# Asides from inlining any simple function, Grappler will also try to lower
# while loop into switch merge representation which is undesired for Ophints,
# so we simply remove those attributes to prevent Grappler from doing so.
graph_def = _convert_to_constants.disable_lower_using_switch_merge(
    sess.graph_def)
config = get_grappler_config(["function"])
graph_def = run_graph_optimizations(
    graph_def, input_tensors, output_tensors, config, graph=sess.graph)

# If ophints are present, just convert them.
hinted_outputs_nodes = find_all_hinted_output_nodes(sess)
if hinted_outputs_nodes:
    exit(_convert_op_hints_if_present(sess, graph_def, output_tensors,
                                        hinted_outputs_nodes))

if not is_frozen_graph(sess):
    output_node_names = [tensor.name.split(":")[0] for tensor in output_tensors]
    exit(tf_graph_util.convert_variables_to_constants(sess, graph_def,
                                                        output_node_names))
else:
    exit(sess.graph_def)
