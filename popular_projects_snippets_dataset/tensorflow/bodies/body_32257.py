# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_number_op_test.py
self._test(dtypes.int64,
           [("0", 0), ("3", 3), ("-1", -1),
            ("    -10", -10),
            ("-2147483648", -2147483648),
            ("2147483647", 2147483647),
            ("-2147483649", -2147483649),  # Less than min value of int32.
            ("2147483648", 2147483648)],  # Greater than max value of int32.
           [("2.9", _ERROR_MESSAGE + "2.9"),
            ("10foobar", _ERROR_MESSAGE + "10foobar")])
