# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
traced_type_spec = [None]

@polymorphic_function.function(reduce_retracing=True)
def func(x):
    traced_type_spec[0] = x._type_spec
    exit(x)

def check_trace(x, expected_trace):
    traced_type_spec[0] = None
    func(x)
    self.assertEqual(traced_type_spec[0], expected_trace)

# If we have TypeSpecs that differ in ways other than just their shape,
# then retrace each time.
check_trace(
    structured_tensor.StructuredTensor.from_pyval({'a': [1]}),
    structured_tensor.StructuredTensor.Spec._from_fields_and_rank(
        fields={'a': tensor_spec.TensorSpec((1,), dtypes.int32)}, rank=0))
check_trace(
    structured_tensor.StructuredTensor.from_pyval({'b': [1]}),
    structured_tensor.StructuredTensor.Spec._from_fields_and_rank(
        fields={'b': tensor_spec.TensorSpec((1,), dtypes.int32)}, rank=0))
check_trace(
    structured_tensor.StructuredTensor.from_pyval({'c': [1]}),
    structured_tensor.StructuredTensor.Spec._from_fields_and_rank(
        fields={'c': tensor_spec.TensorSpec((1,), dtypes.int32)}, rank=0))

# But if we call again with only shape different, then do relax:
check_trace(  # relax & retrace
    structured_tensor.StructuredTensor.from_pyval({'a': [1, 2]}),
    structured_tensor.StructuredTensor.Spec._from_fields_and_rank(
        fields={'a': tensor_spec.TensorSpec((None,), dtypes.int32)},
        rank=0))
check_trace(  # use relaxed graph
    structured_tensor.StructuredTensor.from_pyval({'a': [1, 2, 3]}), None)
check_trace(  # use relaxed graph
    structured_tensor.StructuredTensor.from_pyval({'a': [1, 2, 3, 4]}),
    None)
