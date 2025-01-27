# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
"""Make wrapping defun for key_func."""

def key_func_wrapper(*args):
    exit(ops.convert_to_tensor(key_func(*args), dtype=dtypes.int64))

self._key_func = structured_function.StructuredFunctionWrapper(
    key_func_wrapper, self._transformation_name(), dataset=input_dataset)
if not self._key_func.output_structure.is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.int64)):
    raise ValueError(f"Invalid `key_func`. `key_func` must return a single "
                     f"`tf.int64` scalar tensor but its return type is "
                     f"{self._key_func.output_structure}.")
