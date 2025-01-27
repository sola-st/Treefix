# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/take_while_op.py
"""See `take_while()` for details."""

self._input_dataset = input_dataset
wrapped_func = structured_function.StructuredFunctionWrapper(
    predicate, self._transformation_name(), dataset=self._input_dataset)

if not wrapped_func.output_structure.is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.bool)):
    raise ValueError(f"Invalid `predicate`. `predicate` must return a "
                     f"`tf.bool` scalar tensor but its return type is"
                     f"{wrapped_func.output_structure}.")

self._predicate = wrapped_func
self._name = name
variant_tensor = ged_ops.take_while_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    other_arguments=self._predicate.function.captured_inputs,
    predicate=self._predicate.function,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
