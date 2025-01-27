# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
float_inputs_ = [
    0, 1, -1, 0.5, 0.25, 0.125, float("INF"), float("NAN"), float("-INF")
]

with self.cached_session():
    for dtype in (dtypes.half, dtypes.bfloat16, dtypes.float32,
                  dtypes.float64):
        input_ = array_ops.placeholder(dtype)

        output = string_ops.as_string(input_, shortest=True)
        result = output.eval(feed_dict={input_: float_inputs_})
        s = lambda strs: [x.decode("ascii") for x in strs]
        self.assertAllEqual(s(result), ["%g" % x for x in float_inputs_])

        output = string_ops.as_string(input_, scientific=True)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%e" % x for x in float_inputs_])

        output = string_ops.as_string(input_)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%f" % x for x in float_inputs_])

        output = string_ops.as_string(input_, width=3)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%3f" % x for x in float_inputs_])

        output = string_ops.as_string(input_, width=3, fill="0")
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%03f" % x for x in float_inputs_])

        output = string_ops.as_string(input_, width=3, fill="0", shortest=True)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%03g" % x for x in float_inputs_])

        output = string_ops.as_string(input_, precision=10, width=3)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%03.10f" % x for x in float_inputs_])

        output = string_ops.as_string(
            input_, precision=10, width=3, fill="0", shortest=True)
        result = output.eval(feed_dict={input_: float_inputs_})
        self.assertAllEqual(s(result), ["%03.10g" % x for x in float_inputs_])

    with self.assertRaisesOpError("Cannot select both"):
        output = string_ops.as_string(input_, scientific=True, shortest=True)
        output.eval(feed_dict={input_: float_inputs_})

    with self.assertRaisesOpError("Fill string must be one or fewer"):
        output = string_ops.as_string(input_, fill="ab")
        output.eval(feed_dict={input_: float_inputs_})
