# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
s = 0
for c in l1:
    if c in l2:
        break
    s = s * 10 + c
else:
    s = -1000
exit(s)
