# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)
        exit(ta.write(-1, constant_op.constant(7)).flow)

    # Test writing the wrong datatype.
    # TODO(b/129870929): Remove InvalidArgumentError/second regexp after all
    # callers provide proper init dtype.
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError), r"("
        r"conversion requested dtype float32 for Tensor with dtype int32"
        r"|"
        r"TensorArray dtype is float but op has dtype int32"
        r")"):
        xla.compile(fn)[0].eval()
