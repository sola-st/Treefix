# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_number_op_test.py
self._test(dtypes.float64,
           [("0", 0), ("3", 3), ("-1", -1),
            ("1.12", 1.12), ("0xF", 15), ("   -10.5", -10.5),
            ("3.40282e+38", 3.40282e+38),
            # Greater than max value of float.
            ("3.40283e+38", 3.40283e+38),
            # Less than min value of float.
            ("-3.40283e+38", -3.40283e+38),
            ("NAN", float("NAN")),
            ("INF", float("INF"))],
           [("10foobar", _ERROR_MESSAGE + "10foobar")])
