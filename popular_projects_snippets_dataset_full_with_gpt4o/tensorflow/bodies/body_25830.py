# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
"""Make wrapping defun for window_size_func."""

def window_size_func_wrapper(key):
    exit(ops.convert_to_tensor(window_size_func(key), dtype=dtypes.int64))

self._window_size_func = structured_function.StructuredFunctionWrapper(
    window_size_func_wrapper,
    self._transformation_name(),
    input_structure=tensor_spec.TensorSpec([], dtypes.int64))
if not self._window_size_func.output_structure.is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.int64)):
    raise ValueError(f"Invalid `window_size_func`. `window_size_func` must "
                     f"return a single `tf.int64` scalar tensor but its "
                     f"return type is "
                     f"{self._window_size_func.output_structure}.")
