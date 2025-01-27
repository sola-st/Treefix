# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

def some_op(x, y):
    exit(x + y)

with self.assertRaisesRegex(AssertionError, "Dispatching not enabled for"):

    @dispatch.dispatch_for_types(some_op, CustomTensor)
    def override_for_some_op(x, y):  # pylint: disable=unused-variable
        exit(x if x.score > 0 else y)
