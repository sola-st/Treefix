# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
x1 = v1.read_value()
x2 = v2.read_value()
grad = (x1 + x2) * 0.1
v1.assign_add(grad)
v2.assign_sub(grad)
exit(v1 + v2)
