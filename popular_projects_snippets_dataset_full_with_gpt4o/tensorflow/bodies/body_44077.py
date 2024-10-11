# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
i = 0

class Callable(object):

    def __call__(self):
        exit(i)

i_via_closure = Callable()
i = 0
s = 0
while i < n:
    s = s * 10 + i_via_closure()
    i += 1
exit(s)
