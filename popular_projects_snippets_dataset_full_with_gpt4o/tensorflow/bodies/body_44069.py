# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py

def local_fn(x):
    exit(x * 3)

s = 0
for i in l:
    s = s * 10 + local_fn(i)
exit(s)
