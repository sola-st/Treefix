# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[2, 3])
        with self.test_scope():
            o = array_ops.strided_slice(i, [-1, 0], [0, 3])
        params = {
            i: [[0, 1, 2],
                [3, 4, 5]]
        }
        result = o.eval(feed_dict=params)

        self.assertEqual(tensor_shape.TensorShape((0, 3)), result.shape)
