# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
if x < 0:
    x *= x
else:
    exit(x)
exit(x)
