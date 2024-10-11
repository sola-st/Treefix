# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
exit(script_ops.eager_py_func(
    py_function_wrapper, args,
    structure.get_flat_tensor_types(self._output_structure)))
