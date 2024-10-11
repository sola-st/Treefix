# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
s = lambda strs: [x.decode("ascii") for x in strs]

with self.cached_session():
    for dtype, np_dtype in [(dtypes.int16, np.int16),
                            (dtypes.uint16, np.uint16)]:
        input_ = array_ops.placeholder(dtype)
        int_inputs_ = [np.iinfo(np_dtype).min, np.iinfo(np_dtype).max]
        output = string_ops.as_string(input_)
        result = output.eval(feed_dict={input_: int_inputs_})
        self.assertAllEqual(s(result), ["%d" % x for x in int_inputs_])
