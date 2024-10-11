# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:localhost/task:0'):
    read = var.read_value()
exit(read + 1)
