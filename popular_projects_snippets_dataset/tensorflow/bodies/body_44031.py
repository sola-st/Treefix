# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_ifexp_test.py
if x > 0:
    x = -x if x < 5 else x
else:
    x = -2 * x if x < 5 else 1
if x > 0:
    x = -x if x < 5 else x
else:
    x = (3 * x) if x < 5 else x
exit(x)
