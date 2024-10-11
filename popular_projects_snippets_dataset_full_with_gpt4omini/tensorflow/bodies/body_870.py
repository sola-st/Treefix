# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        with self.test_scope():
            i = array_ops.placeholder(dtype, shape=[2, 4])
            begin = array_ops.placeholder(dtypes.int32, shape=[2])
            end = math_ops.add(begin, [1, 1])
            o = array_ops.strided_slice(i, begin, end, [1, 1])
        params = {
            i: [[0, 1, 2, 3], [4, 5, 6, 7]],
            begin: [1, 1]
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([[5]], result)
