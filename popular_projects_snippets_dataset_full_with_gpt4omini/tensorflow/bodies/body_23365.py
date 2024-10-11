# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run INT8 calibration with the provided input generator function."""
for inp in calibration_input_fn():
    args, kwargs = _convert_to_tensor(inp)
    self._converted_func(*args, **kwargs)

self._for_each_trt_node(self._converted_graph_def, _save_calibration_table)

# Rebuild the function since calibration has changed the graph.
self._converted_func = _construct_function_from_graph_def(
    self._converted_func, self._converted_graph_def)
self._calibrated = True
