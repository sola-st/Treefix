# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor_one = array_ops.reshape(math_ops.range(100), [10, 10])
    tensor_two = tensor_one * 10
    format_output = string_ops.string_format("One: {},\nTwo: {}",
                                             (tensor_one, tensor_two))
    out = self.evaluate(format_output)
    expected = ("One: [[0 1 2 ... 7 8 9]\n"
                " [10 11 12 ... 17 18 19]\n"
                " [20 21 22 ... 27 28 29]\n"
                " ...\n"
                " [70 71 72 ... 77 78 79]\n"
                " [80 81 82 ... 87 88 89]\n"
                " [90 91 92 ... 97 98 99]],\n"
                "Two: [[0 10 20 ... 70 80 90]\n"
                " [100 110 120 ... 170 180 190]\n"
                " [200 210 220 ... 270 280 290]\n"
                " ...\n"
                " [700 710 720 ... 770 780 790]\n"
                " [800 810 820 ... 870 880 890]\n"
                " [900 910 920 ... 970 980 990]]")
    self.assertEqual(compat.as_text(out), expected)
