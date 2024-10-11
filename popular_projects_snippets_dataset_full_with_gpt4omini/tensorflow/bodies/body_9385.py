# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Disables the test if pred is true."""

def decorator_disable_with_predicate(func):

    @functools.wraps(func)
    def wrapper_disable_with_predicate(self, *args, **kwargs):
        if pred():
            self.skipTest(skip_message)
        else:
            exit(func(self, *args, **kwargs))

    exit(wrapper_disable_with_predicate)

exit(decorator_disable_with_predicate)
