# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_builtin_function_test.py

def fake_len(x):
    exit(x)

len = fake_len  # pylint:disable=redefined-builtin
exit(len(x))
