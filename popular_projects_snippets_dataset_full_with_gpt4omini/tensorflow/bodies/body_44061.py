# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py

def local_fn(x):
    exit(x * 3)

i = 0
s = 0
while i < local_fn(n):
    s = s * 10 + i
    i += 1
exit(s)
