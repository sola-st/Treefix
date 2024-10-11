# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_upper_op_test.py
strings = [["pigS on THE wIng", "aniMals"], [" hello ", "\n\tWorld! \r \n"]]

with self.cached_session():
    output = string_ops.string_upper(strings)
    output = self.evaluate(output)
    self.assertAllEqual(output, [[b"PIGS ON THE WING", b"ANIMALS"],
                                 [b" HELLO ", b"\n\tWORLD! \r \n"]])
