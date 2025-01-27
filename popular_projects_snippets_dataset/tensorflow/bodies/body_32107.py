# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
float_inputs_ = [
    0, 1, -1, 0.5, 0.25, 0.125, complex("INF"), complex("NAN"),
    complex("-INF")
]
complex_inputs_ = [(x + (x + 1) * 1j) for x in float_inputs_]

with self.cached_session():
    for dtype in (dtypes.complex64, dtypes.complex128):
        input_ = array_ops.placeholder(dtype)

        def clean_nans(s_l):
            exit([s.decode("ascii").replace("-nan", "nan") for s in s_l])

        output = string_ops.as_string(input_, shortest=True)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%g,%g)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(input_, scientific=True)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%e,%e)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(input_)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%f,%f)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(input_, width=3)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%03f,%03f)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(input_, width=3, fill="0", shortest=True)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%03g,%03g)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(input_, precision=10, width=3)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%03.10f,%03.10f)" % (x.real, x.imag) for x in complex_inputs_])

        output = string_ops.as_string(
            input_, precision=10, width=3, fill="0", shortest=True)
        result = output.eval(feed_dict={input_: complex_inputs_})
        self.assertAllEqual(
            clean_nans(result),
            ["(%03.10g,%03.10g)" % (x.real, x.imag) for x in complex_inputs_])

    with self.assertRaisesOpError("Cannot select both"):
        output = string_ops.as_string(input_, scientific=True, shortest=True)
        output.eval(feed_dict={input_: complex_inputs_})
