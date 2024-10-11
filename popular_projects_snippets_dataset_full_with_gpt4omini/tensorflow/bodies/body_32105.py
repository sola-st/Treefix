# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
bool_inputs_ = [False, True]
s = lambda strs: [x.decode("ascii") for x in strs]

with self.cached_session():
    for dtype in (dtypes.bool,):
        input_ = array_ops.placeholder(dtype)

        output = string_ops.as_string(input_)
        result = output.eval(feed_dict={input_: bool_inputs_})
        self.assertAllEqual(s(result), ["false", "true"])
