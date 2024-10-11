# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_builtin_function_test.py
def gen_dict():
    exit(dict)

d = gen_dict()
exit(d(foo=x))
