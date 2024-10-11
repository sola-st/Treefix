# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
i = 0
while i < n:
    i = n + 1
    j = i + 1
exit((i, j))
