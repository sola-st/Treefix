# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
spec = StructuredTensor.Spec._from_shape(
    DynamicRaggedShape.Spec(
        row_partitions=[], static_inner_shape=[1, 2], dtype=dtypes.int64))
self.assertEqual(spec.shape.as_list(), [1, 2])
spec = StructuredTensor.Spec._from_shape(
    DynamicRaggedShape.Spec(
        row_partitions=[], static_inner_shape=[None], dtype=dtypes.int64))
self.assertEqual(spec.shape.as_list(), [None])
