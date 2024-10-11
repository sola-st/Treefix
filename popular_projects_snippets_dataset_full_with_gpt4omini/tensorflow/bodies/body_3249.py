# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Adds calibration statistics to the graph def.

  This function must be run after running the graph with a representative
  dataset. Retrieves calibration statistics from the global calibrator and adds
  them to the corresponding nodes as attributes.

  Args:
    graph_def: GraphDef to add calibration statistics to.
  """
for function_def in graph_def.library.function:
    for node_def in function_def.node_def:
        if node_def.op != 'CustomAggregator':
            continue

        node_id = node_def.attr['id'].s
        try:
            min_val = quantize_model_wrapper.get_min_from_calibrator(node_id)
            max_val = quantize_model_wrapper.get_max_from_calibrator(node_id)
            quantize_model_wrapper.clear_data_from_calibrator(node_id)
            node_def.attr['min'].f = float(min_val)
            node_def.attr['max'].f = float(max_val)
        except ValueError:
            logging.warn(
                (
                    'CustomAggregator id "%s" from FunctionDef "%s" does not have '
                    'min or max values. Parts of this function are not quantized.'
                ),
                node_id.decode('utf-8'),
                function_def.signature.name,
            )
