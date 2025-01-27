# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[10])
        with self.test_scope():
            o = array_ops.slice(i, [2], [4])
        params = {
            i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([2, 3, 4, 5], result)
