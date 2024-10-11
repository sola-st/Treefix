# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
with ops.device('CPU:0'):
    value0 = create_dataset_and_fetch_one([1.])
with ops.device('CPU:1'):
    value1 = create_dataset_and_fetch_one([2.])
exit((value0, value1))
