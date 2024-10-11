# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
gpu_dev = test.gpu_device_name()

with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(gpu_dev):
        stager = data_flow_ops.MapStagingArea([dtypes.float32])
        y = stager.put(1, [v], [0])
        expected_name = gpu_dev if 'gpu' not in gpu_dev else '/device:GPU:0'
        self.assertEqual(y.device, expected_name)
    with ops.device('/cpu:0'):
        _, x = stager.get(1)
        y = stager.peek(1)[0]
        _, z = stager.get()
        self.assertEqual(x[0].device, '/device:CPU:0')
        self.assertEqual(y.device, '/device:CPU:0')
        self.assertEqual(z[0].device, '/device:CPU:0')

g.finalize()
