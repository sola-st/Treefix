# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
# Cannot use values outside -128..127 for test, because we're also
# testing int8
s = lambda strs: [x.decode("ascii") for x in strs]

with self.cached_session():
    input_ = array_ops.placeholder(dtypes.int32)
    int_inputs_ = [np.iinfo(np.int32).min, np.iinfo(np.int32).max]
    output = string_ops.as_string(input_)
    result = output.eval(feed_dict={input_: int_inputs_})
    self.assertAllEqual(s(result), ["%d" % x for x in int_inputs_])

    input_ = array_ops.placeholder(dtypes.int64)
    int_inputs_ = [np.iinfo(np.int64).min, np.iinfo(np.int64).max]
    output = string_ops.as_string(input_)
    result = output.eval(feed_dict={input_: int_inputs_})
    self.assertAllEqual(s(result), ["%d" % x for x in int_inputs_])
