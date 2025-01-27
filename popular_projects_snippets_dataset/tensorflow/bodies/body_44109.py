# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
v.assign(0)
if c:
    v.assign_add(1)
exit(v.read_value())
