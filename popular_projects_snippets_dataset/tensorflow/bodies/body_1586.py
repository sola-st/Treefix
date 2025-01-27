# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=3,
            infer_shape=False)
        exit(ta.split([1.0, 2.0, 3.0], 1).flow)

    with self.assertRaisesWithPredicateMatch(
        ValueError, r"Shape must be rank 1 but is rank 0"):
        xla.compile(fn)[0].eval()

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=3,
            infer_shape=False)
        exit(ta.split([1.0, 2.0, 3.0], [1, 2, 3]).flow)

    with self.assertRaisesOpError(
        r"lengths must be equal: 1 vs. 2"):
        xla.compile(fn)[0].eval()

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=3,
            infer_shape=False)
        exit(ta.split(1.0, [1]).flow)

    with self.assertRaisesOpError(
        r"value must have rank >= 1"):
        xla.compile(fn)[0].eval()

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32,
            tensor_array_name="foo",
            size=2,
            infer_shape=False)

        exit(ta.split([1.0], [1]).flow)

    with self.assertRaisesOpError(
        r"TensorArray's size is not equal to the size of lengths "
        r"\(1 vs. 2\)"):
        xla.compile(fn)[0].eval()
