# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
"""Make wrapping defun for reduce_func."""
nested_dataset = dataset_ops.DatasetSpec(input_dataset.element_spec)
input_structure = (tensor_spec.TensorSpec([], dtypes.int64), nested_dataset)
self._reduce_func = structured_function.StructuredFunctionWrapper(
    reduce_func,
    self._transformation_name(),
    input_structure=input_structure)
if not isinstance(self._reduce_func.output_structure,
                  dataset_ops.DatasetSpec):
    raise TypeError(f"Invalid `reduce_func`. `reduce_func` must return a "
                    f"single `tf.data.Dataset` object but its return type "
                    f"is {self._reduce_func.output_structure}.")
# pylint: disable=protected-access
self._element_spec = (self._reduce_func.output_structure._element_spec)
