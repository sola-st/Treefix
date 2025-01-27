# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_join_op_test.py
input0 = ["a", "b"]
input1 = "a"
input2 = [["b"], ["c"]]

with self.cached_session():
    output = string_ops.string_join([input0, input1])
    self.assertAllEqual(output, [b"aa", b"ba"])

    output = string_ops.string_join([input0, input1], separator="--")
    self.assertAllEqual(output, [b"a--a", b"b--a"])

    output = string_ops.string_join([input0, input1, input0], separator="--")
    self.assertAllEqual(output, [b"a--a--a", b"b--a--b"])

    output = string_ops.string_join([input1] * 4, separator="!")
    self.assertEqual(self.evaluate(output), b"a!a!a!a")

    output = string_ops.string_join([input2] * 2, separator="")
    self.assertAllEqual(output, [[b"bb"], [b"cc"]])

    with self.assertRaises(ValueError):  # Inconsistent shapes
        string_ops.string_join([input0, input2]).eval()
