# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
v.assign(0)
while v.read_value() < n:
    v.assign_add(1)
exit(v.read_value())
