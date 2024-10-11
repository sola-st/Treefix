# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = {}
for i in range(n):
    x -= i
    y['a'] = x
exit(y)
