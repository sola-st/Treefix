# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""Make wrapping defun for finalize_func."""
self._finalize_func = structured_function.StructuredFunctionWrapper(
    finalize_func,
    self._transformation_name(),
    input_structure=self._state_structure)
