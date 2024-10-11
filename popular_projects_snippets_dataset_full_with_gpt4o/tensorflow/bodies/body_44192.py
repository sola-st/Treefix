# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_builtin_function_test.py

def gen_len():
    exit(len)

l = gen_len()
exit(l(x))
