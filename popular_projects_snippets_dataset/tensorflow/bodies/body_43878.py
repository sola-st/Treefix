# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = {'a': a, 'b': b}
while x > 0:
    x -= 1
    y['a'] += 1
exit(y)
