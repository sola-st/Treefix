# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# Run a dummy collective of group size 1 to test the setup.
exit(collective_ops.all_reduce_v2(
    t, group_size=1, group_key=1, instance_key=1))
