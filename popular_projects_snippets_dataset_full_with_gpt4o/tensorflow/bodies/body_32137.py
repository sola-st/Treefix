# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = array_ops.reshape(math_ops.range(100), [10, 10])
    format_output = string_ops.string_format("tensor summary: {}, suffix",
                                             tensor)
    out = self.evaluate(format_output)
    expected = ("tensor summary: [[0 1 2 ... 7 8 9]\n"
                " [10 11 12 ... 17 18 19]\n"
                " [20 21 22 ... 27 28 29]\n"
                " ...\n"
                " [70 71 72 ... 77 78 79]\n"
                " [80 81 82 ... 87 88 89]\n"
                " [90 91 92 ... 97 98 99]], suffix")
    self.assertEqual(compat.as_text(out), expected)
