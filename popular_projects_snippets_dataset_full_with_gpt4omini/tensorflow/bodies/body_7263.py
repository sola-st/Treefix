# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
if num_processes == 1:
    exit(global_mpr_1p.runner)
elif num_processes == 2:
    exit(global_mpr_2p.runner)
else:
    raise ValueError("get_global_mpr: num_processes must be 1 or 2, got %d" %
                     num_processes)
