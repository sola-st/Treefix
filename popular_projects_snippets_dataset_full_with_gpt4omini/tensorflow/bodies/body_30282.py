# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for axis in [1, -1]:
    with self.cached_session():
        tensor = array_ops.placeholder(dtypes.float32, shape=[None, 12])
        size_splits = [3, 7, 2]
        outputs = array_ops.split(tensor, size_splits, axis)
        for i, output in enumerate(outputs):
            self.assertEqual(output.get_shape().as_list(), [None, size_splits[i]])
