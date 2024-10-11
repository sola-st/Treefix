# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
s = 0
for i in l:
    x = i + 2
    s = s * 10 + x
exit(s)
