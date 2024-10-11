# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
s = 1
i = 0
while i < n:
    i += 1
    if i > 10 * n:
        break
    if i == n:
        break
    s = s * 10 + i
exit((i, s))
