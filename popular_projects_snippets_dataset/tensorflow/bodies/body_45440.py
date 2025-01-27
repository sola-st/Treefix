# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
if x > 0:
    with ops.name_scope(''):
        exit(x * x)
else:
    exit(x)
