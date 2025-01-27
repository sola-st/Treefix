# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reshape_op_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[2, 3])
        with self.test_scope():
            shape = constant_op.constant([3, 2], dtype=index_dtype)
            o = array_ops.reshape(i, shape)
        params = {
            i: [[1, 2, 3], [4, 5, 6]],
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([[1, 2], [3, 4], [5, 6]], result)
