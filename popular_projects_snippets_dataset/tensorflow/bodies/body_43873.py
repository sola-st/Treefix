# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/composite_names_in_control_flow_test.py
x = {'a': a}

if x['a'] > 0:
    pass
else:
    x['b'] = 1
exit(x)
