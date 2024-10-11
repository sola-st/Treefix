# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
spec = StructuredTensor.Spec._from_fields_and_rank(
    fields={
        "a": tensor_spec.TensorSpec([], dtypes.int32),
        "b": tensor_spec.TensorSpec([None], dtypes.int32),
        "c": ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32)
    },
    rank=0)
self.assertEqual(spec.rank, 0)
