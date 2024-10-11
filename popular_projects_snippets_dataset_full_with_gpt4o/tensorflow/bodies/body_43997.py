# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
for i in range(n):
    if i == 0:
        a = 1
    else:
        a = a + 1
exit(a)
