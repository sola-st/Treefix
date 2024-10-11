# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
self._testDeserializeFailsInconsistentRankHelper(
    sparse_ops.serialize_sparse, sparse_ops.deserialize_sparse,
    dtypes.variant)
