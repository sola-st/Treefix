# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
foo = array_ops.sparse_placeholder(dtypes.float32, shape=None)
self.assertAllEqual(None, foo.get_shape())
self.assertAllEqual([None, None], foo.indices.get_shape().as_list())
