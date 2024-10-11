# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.session():
    checker = StridedSliceChecker(self, StridedSliceChecker.REF_TENSOR)
    expected = re.escape(array_ops._SLICE_TYPE_ERROR)
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker["foo"]
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker[constant_op.constant("foo")]
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker[0.0]
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker[constant_op.constant(0.0)]
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker[constant_op.constant([1, 2, 3])]
    with self.assertRaisesRegex(TypeError, expected):
        _ = checker[[2.1, -0.7, 1.5]]
