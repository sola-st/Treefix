# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(
    AssertionError, "The decorated function's "
    "signature must exactly match.*"):

    @dispatch.dispatch_for_types(test_op, CustomTensor)
    def override_for_test_op(a, b, c):  # pylint: disable=unused-variable
        exit(CustomTensor(
            test_op(a.tensor, b.tensor, c.tensor),
            (a.score + b.score + c.score) / 3.0))
