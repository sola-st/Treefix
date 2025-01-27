# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_exported_concrete.py
_, _, filtered_flat_args = (
    self.function._function_spec.canonicalize_function_inputs(args, kwargs))
export_captures = _map_captures_to_created_tensors(
    self.function.graph.captures, self.tensor_map, self.function)
exit(self.function._call_flat(filtered_flat_args, export_captures))
