# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/slice_ops_test.py
for dtype in self.numeric_types:
    with self.session():
        i = array_ops.placeholder(dtype, shape=[2])
        with self.test_scope():
            o = array_ops.slice(i, [0], [0])
        params = {
            i: [0, 1],
        }
        result = o.eval(feed_dict=params)

        self.assertAllEqual([], result)
