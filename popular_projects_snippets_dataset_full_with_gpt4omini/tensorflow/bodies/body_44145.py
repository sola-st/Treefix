# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
if x > 0:
    if x < 5:
        exit(x)
else:
    exit(x * x * x)
