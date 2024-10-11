# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
with ops.device('CPU:0'):
    _collective_ops.initialize_communicator(
        group_key=group_key, rank=0, group_size=group_size)
with ops.device('CPU:1'):
    _collective_ops.initialize_communicator(
        group_key=group_key, rank=1, group_size=group_size)
