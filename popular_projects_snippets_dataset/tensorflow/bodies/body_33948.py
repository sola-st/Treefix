# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
gpu_dev = test.gpu_device_name()

with ops.Graph().as_default() as G:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(gpu_dev):
        stager = data_flow_ops.StagingArea([dtypes.float32])
        y = stager.put([v])
        expected_name = gpu_dev if 'gpu' not in gpu_dev else '/device:GPU:0'
        self.assertEqual(y.device, expected_name)
    with ops.device('/cpu:0'):
        x = stager.get()[0]
        self.assertEqual(x.device, '/device:CPU:0')

G.finalize()
