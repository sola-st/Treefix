# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[3, 3, 10])
        with self.test_scope():
            o = array_ops.strided_slice(i, [0, 2, 2], [2, 3, 6], [1, 1, 2])
        params = {
            i: [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                 [5, 3, 1, 7, 9, 2, 4, 6, 8, 0]],
                [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [8, 7, 6, 5, 4, 3, 2, 1, 8, 7]],
                [[7, 5, 7, 5, 7, 5, 7, 5, 7, 5],
                 [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                 [9, 8, 7, 9, 8, 7, 9, 8, 7, 9]]]
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([[[1, 9]], [[6, 4]]], result)
