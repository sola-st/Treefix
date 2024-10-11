# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('cpu:0'):
    # Multiple CPU:0 devices match would be found, but the CPU:0 from the
    # parent device scope should be picked.
    x = test_ops.device_placement_op()
    y = string_ops.string_upper(x)
    packed_var_0 = array_ops.stack([x, y], 0)
    exit(packed_var_0)
