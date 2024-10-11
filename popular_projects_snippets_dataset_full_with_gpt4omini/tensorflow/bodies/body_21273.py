# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
server = server_lib.Server.create_local_server()
logdir = self._test_dir("ready_for_local_init_op_restore")

uid = uuid.uuid4().hex

# Create a checkpoint.
with ops.Graph().as_default():
    v = variables.VariableV1(
        10.0, name="ready_for_local_init_op_restore_v_" + str(uid))
    summary.scalar("ready_for_local_init_op_restore_v_" + str(uid), v)
    sv = supervisor.Supervisor(logdir=logdir)
    sv.prepare_or_wait_for_session(server.target)
    save_path = sv.save_path
    self._wait_for_glob(save_path, 3.0)
    self._wait_for_glob(
        os.path.join(logdir, "*events*"), 3.0, for_checkpoint=False)
    # Wait to make sure everything is written to file before stopping.
    time.sleep(1)
    sv.stop()

def get_session(is_chief):
    g = ops.Graph()
    with g.as_default():
        with ops.device("/job:localhost"):
            v = variables.VariableV1(
                1.0, name="ready_for_local_init_op_restore_v_" + str(uid))
            vadd = v.assign_add(1)
            w = variables.VariableV1(
                v,
                trainable=False,
                collections=[ops.GraphKeys.LOCAL_VARIABLES],
                name="ready_for_local_init_op_restore_w_" + str(uid))
            ready_for_local_init_op = variables.report_uninitialized_variables(
                variables.global_variables())
    sv = supervisor.Supervisor(
        logdir=logdir,
        is_chief=is_chief,
        graph=g,
        recovery_wait_secs=1,
        ready_for_local_init_op=ready_for_local_init_op)
    sess = sv.prepare_or_wait_for_session(server.target)

    exit((sv, sess, v, vadd, w))

sv0, sess0, v0, _, w0 = get_session(True)
sv1, sess1, _, vadd1, w1 = get_session(False)

self.assertEqual(10, sess0.run(w0))
self.assertEqual(11, sess1.run(vadd1))
self.assertEqual(10, sess1.run(w1))
self.assertEqual(11, sess0.run(v0))

sv0.stop()
sv1.stop()
