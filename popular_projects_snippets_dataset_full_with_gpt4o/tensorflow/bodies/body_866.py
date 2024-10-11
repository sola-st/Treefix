# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[10])
        begin = array_ops.placeholder(dtypes.int32, shape=[1])
        with self.test_scope():
            end = math_ops.add(begin, [1])
            o = array_ops.strided_slice(i, begin, end, [1])
        params = {
            i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            begin: [0]
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([0], result)
