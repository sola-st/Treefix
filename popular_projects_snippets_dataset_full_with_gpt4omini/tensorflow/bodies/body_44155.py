# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
try:
    if x > 0:
        exit(0)
finally:
    exit(1)  # pylint: disable=lost-exception
