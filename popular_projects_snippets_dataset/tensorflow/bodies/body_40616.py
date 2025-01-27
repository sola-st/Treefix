# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with ops.device(self.device_t1):
    mul = math_ops.matmul(i, i)
exit(mul - array_ops.zeros_like(mul))
