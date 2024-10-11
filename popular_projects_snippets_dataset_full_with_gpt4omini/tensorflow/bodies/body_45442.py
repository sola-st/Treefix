# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
with ops.name_scope(''):
    if x > 0:
        exit(x * x)
    else:
        exit(x)
