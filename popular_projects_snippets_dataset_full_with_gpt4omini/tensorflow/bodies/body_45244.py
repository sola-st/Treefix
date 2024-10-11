# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
for i in n:
    if i == 0:
        result = i - 1
    if i > 0:  # Using the result from previous iteration.
        if result < 0:
            x += 1
exit(x)
