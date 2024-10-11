# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
# index is 0 on CPU and 1 on GPU
index = gen_functional_ops.DeviceIndex(device_names=["CPU", "GPU"])
exit(in_t + math_ops.cast(index, dtypes.float32))
