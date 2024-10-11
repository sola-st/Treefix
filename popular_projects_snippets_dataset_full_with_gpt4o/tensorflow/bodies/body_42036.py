# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
c = x + y
# Multiple outputs from split.
d, f = array_ops.split(c, 2)
exit(d + f)
