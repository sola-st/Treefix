# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
res = []
for t, d in zip(tensors, devices):
    with ops.device(d):
        res.append(array_ops.identity(t))
exit(res)
