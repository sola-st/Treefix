# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
composite_tensor = ragged_tensor.RaggedTensor.from_row_splits(
    values=[1, 2, 3], row_splits=[0, 2, 3])
spec = ragged_tensor.RaggedTensorSpec([2, None], dtypes.int32)

self.assertEqual(
    trace_type.from_value(composite_tensor), trace_type.from_value(spec))
