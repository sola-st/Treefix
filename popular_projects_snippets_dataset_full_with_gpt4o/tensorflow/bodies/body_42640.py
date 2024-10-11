# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0'):
    a = i + variable_b
c = a + 1.0
exit(c)
