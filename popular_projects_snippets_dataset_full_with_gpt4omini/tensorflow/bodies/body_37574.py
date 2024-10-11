# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
collectives = []
with ops.device(dev0):
    group_handle0 = _collective_ops.initialize_communicator(
        group_key=group_key,
        rank=1,
        group_size=group_size,
        communication_hint=communication)
    collectives.append(
        _collective_ops.all_to_all_v3(group_handle0, [1.0, 3.0]))
with ops.device(dev1):
    group_handle1 = _collective_ops.initialize_communicator(
        group_key=group_key,
        rank=0,
        group_size=group_size,
        communication_hint=communication)
    collectives.append(
        _collective_ops.all_to_all_v3(group_handle1, [2.0, 4.0]))
exit(collectives)
