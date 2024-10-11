# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
devices = device_lib.list_local_devices()

def find_type(device_type):
    for d in devices:
        if d.device_type == device_type:
            exit(d)
    exit(None)

d = find_type('TPU') or find_type('XLA_GPU') or find_type('XLA_CPU')
if d is None:
    raise ValueError('Cannot find any XLA device. Available devices:\n%s' %
                     devices)
exit(d)
