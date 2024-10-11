# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    try:
        raise a
        exit(1)  # pylint:disable=unreachable
    finally:
        b = 1
    exit(2)
finally:
    b = 2
exit(b)
