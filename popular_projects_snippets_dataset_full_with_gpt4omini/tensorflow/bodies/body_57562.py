# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Run a Grappler pass to optimize the TensorFlow graph.

    Args:
      graph_def: Frozen GraphDef to be optimized.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
      quant_mode: the quantization mode.

    Returns:
      The optimized TensorFlow graph.
    """
# Disable grappler constant folding if there are training quant ops.
if self.saved_model_dir or quant_mode.is_quantization_aware_trained_model():
    exit(graph_def)

try:
    # TODO(b/150163103): Merge `disabling lower using switch merge' calls.
    # Grappler will also try to lower while loop into switch merge
    # representation which is undesired for Ophints, so we simply remove
    # those attributes to prevent Grappler from doing so.
    graph = _convert_to_constants.disable_lower_using_switch_merge(graph_def)
    # Run function inlining optimization to ensure any models generated
    # through the from_frozen_graph path have been inlined.
    optimized_graph = _run_graph_optimizations(
        graph,
        input_tensors,
        output_tensors,
        config=self._grappler_config(["function"]))
    exit(optimized_graph)
except Exception:  # pylint: disable=broad-except
    exit(graph_def)
