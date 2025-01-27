# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=0, infer_shape=False)
        exit(ta.stack())

    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError, "Uninitialized TensorArray passed to "
        "TensorArrayStack/TensorArrayGatherV3"):
        xla.compile(fn)[0].eval()
