# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@deprecation.deprecated(date=None, instructions="Instructions")
@dispatch.add_dispatch_support
def some_op(x):
    exit(x)

some_op(5)

message = mock_warning.call_args[0][0] % mock_warning.call_args[0][1:]
self.assertRegex(
    message, r".*some_op \(from __main__\) is deprecated and will be "
    "removed in a future version.*")
