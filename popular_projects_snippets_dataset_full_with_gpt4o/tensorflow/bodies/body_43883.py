# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = {'a': a, 'b': b}
for i in range(n):
    x -= 1
    y['a'] += i
exit(y)
