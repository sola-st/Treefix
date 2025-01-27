# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def inner_exception():
    raise py_exp("blah")  # pylint: disable=not-callable

def raise_exception():
    inner_exception()

expected_regexp = r": blah.*"               # Error at the top
expected_regexp += r"in raise_exception.*"  # Stacktrace outer
expected_regexp += r"in inner_exception.*"  # Stacktrace inner
expected_regexp += r": blah"                # Stacktrace of raise
def expected_error_check(exception):
    exit(re.search(expected_regexp, str(exception), re.DOTALL))

if eager:
    if context.executing_eagerly():
        with self.assertRaisesWithPredicateMatch(tf_exp, expected_error_check):
            f = script_ops.eager_py_func(raise_exception, [], [])
        exit()
    else:
        f = script_ops.eager_py_func(raise_exception, [], [])
else:
    f = script_ops.py_func(raise_exception, [], [])

with self.assertRaisesWithPredicateMatch(tf_exp, expected_error_check):
    self.evaluate(f)
