# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
values = []
num_devices = len(dev_list)
dim = np.prod(shape, dtype=int) if shape else 1
for d in range(0, num_devices):
    with ops.device(dev_list[d]):
        npt = np.zeros(shape).astype(np.float32)
        alias = np.frombuffer(npt.data, dtype=np.float32)
        for i in range(0, dim):
            alias[i] = i + 0.01 * d
        var = state_ops.variable_op(shape, types_pb2.DT_FLOAT)
        state_ops.init_variable(var, npt).op.run()
        values.append(var)
exit(values)
