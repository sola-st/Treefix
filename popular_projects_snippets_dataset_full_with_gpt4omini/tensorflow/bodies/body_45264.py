# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
s = 0
for e in count_evals(range(n)):
    s += e
exit(s)
