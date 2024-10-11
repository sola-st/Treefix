# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = _make_ta(3, "foo", dtype=dtypes.float32)

    w0 = ta.write(0, [[4.0, 5.0]])

    # Test reading wrong datatype (only possible when constructing graphs).
    if (not context.executing_eagerly() and
        not control_flow_util.ENABLE_CONTROL_FLOW_V2):
        r0_bad = gen_data_flow_ops.tensor_array_read_v3(
            handle=w0.handle, index=0, dtype=dtypes.float64, flow_in=w0.flow)
        with self.assertRaisesOpError(
            "TensorArray dtype is float but Op requested dtype double."):
            self.evaluate(r0_bad)

    if (control_flow_util.ENABLE_CONTROL_FLOW_V2 and
        not context.executing_eagerly()):
        error_msg = "Trying to access element -1 in a list with 3 elements."
    else:
        error_msg = "index -1"
    # Test reading from a negative index, which is not allowed
    with self.assertRaisesOpError(error_msg):
        self.evaluate(ta.read(-1))

    if (control_flow_util.ENABLE_CONTROL_FLOW_V2 and
        not context.executing_eagerly()):
        error_msg = "Trying to access element 3 in a list with 3 elements."
    else:
        error_msg = "Tried to read from index 3 but array size is: 3"
    # Test reading from too large an index
    with self.assertRaisesOpError(error_msg):
        self.evaluate(ta.read(3))
