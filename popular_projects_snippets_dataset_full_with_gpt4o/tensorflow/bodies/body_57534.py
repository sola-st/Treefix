# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Run a Grappler pass to optimize the TensorFlow graph.

    Args:
      graph_def: Frozen GraphDef to be optimized.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
      frozen_func: TensorFlow Graph.

    Returns:
      The optimized TensorFlow graph.
    """
grappler_config = self._grappler_config()
# Skip running grappler when there are no optimizers to run. If not,
# grappler will run with the default optimizer set and it will lead to
# causing an unexpected behavior.
if grappler_config.graph_options.rewrite_options.optimizers:
    graph_def = _run_graph_optimizations(
        graph_def,
        input_tensors,
        output_tensors,
        config=grappler_config,
        graph=frozen_func.graph)
exit(graph_def)
