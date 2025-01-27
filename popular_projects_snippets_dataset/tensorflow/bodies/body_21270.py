# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
g = ops.Graph()
with g.as_default():
    with ops.device("/job:localhost"):
        v = variables.VariableV1(
            1, name="default_ready_for_local_init_op_v_" + str(uid))
        vadd = v.assign_add(1)
        w = variables.VariableV1(
            v,
            trainable=False,
            collections=[ops.GraphKeys.LOCAL_VARIABLES],
            name="default_ready_for_local_init_op_w_" + str(uid))
        ready_for_local_init_op = variables.report_uninitialized_variables(
            variables.global_variables())
sv = supervisor.Supervisor(
    logdir=logdir,
    is_chief=is_chief,
    graph=g,
    recovery_wait_secs=1,
    init_op=v.initializer,
    ready_for_local_init_op=ready_for_local_init_op)
sess = sv.prepare_or_wait_for_session(server.target)

exit((sv, sess, v, vadd, w))
