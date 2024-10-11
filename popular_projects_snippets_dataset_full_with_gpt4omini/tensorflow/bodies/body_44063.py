# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py

def local_fn(l):
    exit(l * 1)

s = 0
for i in local_fn(l):
    s = s * 10 + i
exit(s)
