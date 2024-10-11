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

check_trace(  # Initial call gets traced.
    ragged_factory_ops.constant([[1], [2, 3, 4]]),
    ragged_tensor.RaggedTensorSpec([2, None], dtypes.int32))
check_trace(  # Input TypeSpec is the same -> no retrace.
    ragged_factory_ops.constant([[1, 2], [3, 4]]), None)
check_trace(  # Even if component tensor shapes change -> no retrace.
    ragged_factory_ops.constant([[1, 2], [3, 4, 5, 6]]), None)
check_trace(  # Different TypeSpec shape (nrows): relax & retrace
    ragged_factory_ops.constant([[1], [2], [3]]),
    ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32))
check_trace(  # Different nrows again: relax & retrace
    ragged_factory_ops.constant([[1], [2], [3], [4]]), None)
check_trace(  # Different nrows yet again: not retrace
    ragged_factory_ops.constant([[1]]), None)
check_trace(  # Different ragged_rank: retrace
    ragged_factory_ops.constant([[[1]]]),
    ragged_tensor.RaggedTensorSpec([1, None, None], dtypes.int32))
check_trace(  # Different ragged_rank again: retrace & relax
    ragged_factory_ops.constant([[[1]], [[2]]]),
    ragged_tensor.RaggedTensorSpec([None, None, None], dtypes.int32))
