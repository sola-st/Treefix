# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
server = server_lib.Server.create_local_server()
logdir = self._test_dir("default_init_op_fails_for_local_variable")
with ops.Graph().as_default():
    v = variables.VariableV1(
        [1.0, 2.0, 3.0],
        name="v",
        collections=[ops.GraphKeys.LOCAL_VARIABLES])
    variables.VariableV1(
        [1.0, 2.0, 3.0],
        name="w",
        collections=[ops.GraphKeys.LOCAL_VARIABLES])
    # w will not be initialized.
    sv = supervisor.Supervisor(logdir=logdir, local_init_op=v.initializer)
    with self.assertRaisesRegex(RuntimeError, "Variables not initialized: w"):
        sv.prepare_or_wait_for_session(server.target)
