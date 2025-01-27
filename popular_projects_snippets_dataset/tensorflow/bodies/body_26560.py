# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""Make wrapping defun for key_func."""
self._key_func = structured_function.StructuredFunctionWrapper(
    key_func, self._transformation_name(), dataset=input_dataset)
if not self._key_func.output_structure.is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.int64)):
    raise ValueError(
        f"Invalid `key_func`. Expected `key_func` to return a scalar "
        f"tf.int64 tensor, but instead `key_func` has output "
        f"types={self._key_func.output_types} "
        f"and shapes={self._key_func.output_shapes}."
    )
