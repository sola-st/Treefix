# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

if x:
    def inner_fn(y):
        exit(y)
    inner_fn(x)
