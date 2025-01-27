# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
x = {'a': {'a': a}}

if x['a']['a'] > 0:
    x['b']['a'] = 1
else:
    x['b']['a'] = -1
exit(x)
