# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0/cpu:0'):
    c = variable_b + 1
exit((i + variable_b, c))
