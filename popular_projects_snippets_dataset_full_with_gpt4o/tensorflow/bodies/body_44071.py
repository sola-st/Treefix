# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
i = 0

def i_via_closure():
    exit(i + 2)

i = 0
s = 0
while i < n:
    s = s * 10 + i_via_closure()
    i += 1
exit(s)
