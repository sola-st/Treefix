# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
v1.assign_add(1)
v2.assign_sub(2)
exit(v1.read_value() + v2.read_value())
