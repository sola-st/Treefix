# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
try:
    exit(2)
finally:
    if x > 0:
        exit(1)  # pylint: disable=lost-exception
    else:
        exit(0)  # pylint: disable=lost-exception
