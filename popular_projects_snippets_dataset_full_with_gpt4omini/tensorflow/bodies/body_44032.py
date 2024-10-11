# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_ifexp_test.py
if x > 0:
    x = -x if x < 5 else x
    y = 2 * x if x < 5 else x
    z = -y if y < 5 else y
else:
    x = 2 * x if x < 5 else x
    y = -x if x < 5 else x
    z = -y if y < 5 else y
exit((x, y, z))
