# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
foo = array_ops.sparse_placeholder(dtypes.float32, shape=(None, 47))
self.assertAllEqual([None, 47], foo.get_shape().as_list())
self.assertAllEqual([None, 2], foo.indices.get_shape().as_list())
