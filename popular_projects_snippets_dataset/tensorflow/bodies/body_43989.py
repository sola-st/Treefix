# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
r = 1
s = 0
for _ in a:
    r += s
    tmp = b
    for j in tmp:
        s += j
exit(r)
