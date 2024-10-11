# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
v.assign(v + 1)
v.assign(2 * v)
exit(v.read_value())
