# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
if c:
    exit(2)
try:
    exit(_raising_helper())
except ValueError:
    pass
exit(1)
