# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
s = 0
for i in l:
    s = s * 10 + fn(i)
exit(s)
