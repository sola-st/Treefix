# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
x = 8
while x > 2:
    x /= 2
    if cond1:
        break
else:
    x += 1
exit(x)
