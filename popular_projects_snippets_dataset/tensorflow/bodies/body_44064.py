# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
i = 0
s = 0
while i < n:
    s = s * 10 + fn(i)
    i += 1
exit(s)
