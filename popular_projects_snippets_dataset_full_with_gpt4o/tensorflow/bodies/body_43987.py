# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
p = 0
for _ in a:
    tmp = b
    for j in tmp:
        p += j
exit(p)
