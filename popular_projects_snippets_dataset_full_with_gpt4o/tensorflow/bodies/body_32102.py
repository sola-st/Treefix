# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
# Cannot use values outside -128..127 for test, because we're also
# testing int8
int_inputs = [0, -1, 1, -128, 127, -101, 101, -0]
int_dtypes = [dtypes.int8, dtypes.int32, dtypes.int64]
uint_inputs = [0, 1, 127, 255, 101]
uint_dtypes = [dtypes.uint8, dtypes.uint32, dtypes.uint64]
s = lambda strs: [x.decode("ascii") for x in strs]

with self.cached_session():
    for dtypes_, inputs in [(int_dtypes, int_inputs),
                            (uint_dtypes, uint_inputs)]:
        for dtype in dtypes_:
            input_ = array_ops.placeholder(dtype)

            output = string_ops.as_string(input_)
            result = output.eval(feed_dict={input_: inputs})
            self.assertAllEqual(s(result), ["%d" % x for x in inputs])

            output = string_ops.as_string(input_, width=3)
            result = output.eval(feed_dict={input_: inputs})
            self.assertAllEqual(s(result), ["%3d" % x for x in inputs])

            output = string_ops.as_string(input_, width=3, fill="0")
            result = output.eval(feed_dict={input_: inputs})
            self.assertAllEqual(s(result), ["%03d" % x for x in inputs])

        with self.assertRaisesOpError("scientific and shortest"):
            output = string_ops.as_string(input_, scientific=True)
            output.eval(feed_dict={input_: inputs})

        with self.assertRaisesOpError("scientific and shortest"):
            output = string_ops.as_string(input_, shortest=True)
            output.eval(feed_dict={input_: inputs})

        with self.assertRaisesOpError("precision not supported"):
            output = string_ops.as_string(input_, precision=0)
            output.eval(feed_dict={input_: inputs})
