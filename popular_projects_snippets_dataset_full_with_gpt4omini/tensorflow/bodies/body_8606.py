# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
c = constant_op.constant([2])

@def_function.function
def send():
    s0 = collective_ops.broadcast_send(
        c * 3, c.shape, c.dtype, group_size=2, group_key=1, instance_key=1)
    with ops.control_dependencies([s0.op]):
        exit(array_ops.identity(c))

@def_function.function
def recv():
    r0 = collective_ops.broadcast_recv(
        c.shape, c.dtype, group_size=2, group_key=1, instance_key=1)
    exit(r0)

exit(control_flow_ops.switch_case(
    device_id, branch_fns={0: send, 1: recv}))
