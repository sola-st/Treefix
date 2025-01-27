# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
if i == 0:
    result = i - 1
else:
    result = i + 1
exit(result)
