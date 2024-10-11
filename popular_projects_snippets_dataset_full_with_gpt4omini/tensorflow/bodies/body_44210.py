# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
for i in range(y):
    if i == 2:
        break
    if x > 0:
        x -= 1
exit(x)
