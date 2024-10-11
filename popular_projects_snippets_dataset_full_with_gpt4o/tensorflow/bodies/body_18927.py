# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/compiled_collective_ops_gpu_test.py
"""Set group_size = num_gpus = 2 for all tests in this class."""
super(CompiledCollectiveOpGPUTest, cls).setUpClass()
# Group size is the number of devices in a group communicating collectively.
# This will be passed into the collective ops in the tests below.
cls._group_size = 2
cls._devices = ['/device:GPU:{}'.format(i) for i in range(2)]
os.environ['NCCL_DEBUG'] = 'INFO'
os.environ['NCCL_LAUNCH_MODE'] = 'PARALLEL'
