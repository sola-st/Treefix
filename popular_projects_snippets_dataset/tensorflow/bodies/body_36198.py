# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# We run two collectives here to make sure we cancel in the middle of the
# RemoteCall. The second one should never finish.
anchor = collective_ops.all_reduce_v2(
    v, group_size=2, group_key=1, instance_key=1)
with ops.control_dependencies([anchor]):
    exit(collective_ops.all_reduce_v2(
        v, group_size=2, group_key=1, instance_key=2))
