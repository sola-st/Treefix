# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = 2
group_key = 105

dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device

@def_function.function
def run_all_to_all_2devices():
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

result = run_all_to_all_2devices()
self.assertAllClose(result[0], [2.0, 1.0], rtol=1e-5, atol=1e-5)
self.assertAllClose(result[1], [4.0, 3.0], rtol=1e-5, atol=1e-5)
