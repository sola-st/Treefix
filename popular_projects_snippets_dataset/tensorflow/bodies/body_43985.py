# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
y = 0
if x > 0:
    try:
        if x > 1:
            _hidden_raise()
        y = 1
    except ValueError:
        pass
    if y == 0:
        y = 2
exit(y)
