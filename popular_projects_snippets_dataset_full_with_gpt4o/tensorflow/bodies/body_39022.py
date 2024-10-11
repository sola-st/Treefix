# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
self._testFeedSerializeDeserializeBatchHelper(sparse_ops.serialize_sparse,
                                              sparse_ops.deserialize_sparse,
                                              dtypes.variant)
