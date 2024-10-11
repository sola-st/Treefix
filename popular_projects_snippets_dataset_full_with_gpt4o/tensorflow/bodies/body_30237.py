# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
dtype = dtypes.int32
for side in ("left", "right"):
    with self.subTest(side=side):
        self.assertAllEqual(
            array_ops.searchsorted(
                array_ops.ones([2, 0]),
                array_ops.ones([2, 3]),
                side=side,
                out_type=dtype), array_ops.zeros([2, 3], dtype))
