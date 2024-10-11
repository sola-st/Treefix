# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
v = []
devices = ["/device:GPU:0", "/device:CPU:0"]
for d, _ in zip(devices, ["v", "v/replica"]):
    with ops.device(d):
        v.append(constant_op.constant(init_val))
exit(values_lib.Mirrored(v))
