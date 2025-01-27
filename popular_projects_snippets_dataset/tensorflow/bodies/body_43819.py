# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
s = 0
for i in l1:
    s = s * 10 + i
for i in l2:
    s = s * 10 + i
exit(s)
