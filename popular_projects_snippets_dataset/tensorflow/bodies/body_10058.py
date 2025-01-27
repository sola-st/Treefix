# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
"""Applies a series of inference optimizations on the input graph.

  Args:
    input_graph_def: A GraphDef containing a training model.
    input_node_names: A list of names of the nodes that are fed inputs during
      inference.
    output_node_names: A list of names of the nodes that produce the final
      results.
    placeholder_type_enum: The AttrValue enum for the placeholder data type, or
        a list that specifies one value per input node name.
    toco_compatible: Boolean, if True, only runs optimizations that result in
      TOCO compatible graph operations (default=False).

  Returns:
    An optimized version of the input graph.
  """
ensure_graph_is_valid(input_graph_def)
optimized_graph_def = input_graph_def
optimized_graph_def = strip_unused_lib.strip_unused(
    optimized_graph_def, input_node_names, output_node_names,
    placeholder_type_enum)
optimized_graph_def = graph_util.remove_training_nodes(
    optimized_graph_def, output_node_names)
optimized_graph_def = fold_batch_norms(optimized_graph_def)
if not toco_compatible:
    optimized_graph_def = fuse_resize_and_conv(optimized_graph_def,
                                               output_node_names)
ensure_graph_is_valid(optimized_graph_def)
exit(optimized_graph_def)
