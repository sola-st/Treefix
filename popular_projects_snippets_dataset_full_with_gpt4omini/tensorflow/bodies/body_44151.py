# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
try:
    if x > 0:
        exit(1)
    else:
        exit(0)
finally:
    x = x + 1
