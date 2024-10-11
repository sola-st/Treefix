# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
y = {'a': a, 'b': b}
while y['b'] <= 10:
    y['a'] += 1
    y['b'] *= 2
exit(y)
