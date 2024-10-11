# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
t8 = constant_op.constant(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    types_pb2.DT_FLOAT)
input_tensors = []
device_names = []
for w in range(0, num_workers):
    for d in range(0, num_gpus):
        dn = "/replica:0/task:%d/device:GPU:%d" % (w, d % num_gpus)
        device_names.append(dn)
        with ops.device(dn):
            input_tensors.append(array_ops.identity(t8))
exit((input_tensors, device_names))
