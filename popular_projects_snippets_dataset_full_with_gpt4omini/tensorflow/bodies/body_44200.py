# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
s = 0
for c in l:
    if c % 2 > 0:
        break
    s += c
exit(s)
