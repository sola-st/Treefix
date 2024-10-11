# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = [a, b]
for i in range(n):
    x -= 1
    y[0] += i
exit(y)
