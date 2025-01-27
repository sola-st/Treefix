# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""Make wrapping defun for init_func."""
self._init_func = structured_function.StructuredFunctionWrapper(
    init_func,
    self._transformation_name(),
    input_structure=tensor_spec.TensorSpec([], dtypes.int64))
