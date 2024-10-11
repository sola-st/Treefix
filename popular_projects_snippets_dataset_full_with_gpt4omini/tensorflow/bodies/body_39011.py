# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
self._testSerializeDeserializeBatchHelper(
    sparse_ops.serialize_sparse, sparse_ops.deserialize_many_sparse)
