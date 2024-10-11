# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
foo = array_ops.sparse_placeholder(dtypes.float32, shape=(10, 47))
self.assertAllEqual([10, 47], foo.get_shape())
self.assertAllEqual([None, 2], foo.indices.get_shape().as_list())
