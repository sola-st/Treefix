# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = _make_ta(3, "foo", dtype=dtypes.float32)
    # TODO(b/129870929): Remove the last 2 checks (runtime checks) after
    # back back from preferred_dtype= to dtype= in convert_to_tensor.  Also
    # restrict error check to only TypeError.
    error_msg_regex = (
        "("
        "Expected float32, got 'wrong_type_scalar' of type 'str' instead."
        "|"
        "Cannot convert provided value to EagerTensor. Provided value: "
        "wrong_type_scalar Requested dtype: float"
        "|"
        "TensorArray dtype is float.* but Op is trying to write dtype string"
        "|"
        "Invalid data types; op elements string but list elements float"
        ")")
    with self.assertRaisesRegex((TypeError, errors.InvalidArgumentError),
                                error_msg_regex):
        self.evaluate(ta.write(0, "wrong_type_scalar").flow)

    if (control_flow_util.ENABLE_CONTROL_FLOW_V2 and
        not context.executing_eagerly()):
        error_msg = "Trying to modify element -1 in a list with 3 elements."
    else:
        error_msg = "index -1"
    with self.assertRaisesOpError(error_msg):
        self.evaluate(ta.write(-1, 3.0).flow)

    if (control_flow_util.ENABLE_CONTROL_FLOW_V2 and
        not context.executing_eagerly()):
        error_msg = "Trying to modify element 3 in a list with 3 elements"
    else:
        error_msg = ("Tried to write to index 3 but array is not "
                     "resizeable and size is: 3")
    # Test reading from too large an index
    with self.assertRaisesOpError(error_msg):
        self.evaluate(ta.write(3, 3.0).flow)
