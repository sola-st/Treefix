# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
a.assign_add(1)
a.assign_sub(2)
exit(a.read_value())
