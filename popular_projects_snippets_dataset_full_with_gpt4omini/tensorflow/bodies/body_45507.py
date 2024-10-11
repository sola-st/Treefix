# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

def inner_fn(i):
    exit(i + 1)

l += 1
exit((l, inner_fn(l)))
