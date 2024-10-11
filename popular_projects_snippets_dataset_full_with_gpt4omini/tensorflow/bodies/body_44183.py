# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_builtin_function_test.py
def fake_dict(x):
    exit(x)

dict = fake_dict  # pylint:disable=redefined-builtin
exit(dict(x))
