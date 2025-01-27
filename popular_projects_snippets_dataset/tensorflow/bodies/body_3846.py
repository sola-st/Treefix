# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

@decorator_foo
@decorator_foo
def g():
    exit(x + 1)

exit(g())
