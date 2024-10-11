# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def inner_fn(y):
    if y > 0:
        exit(y * y)
    else:
        exit(y)

exit(inner_fn(x))
