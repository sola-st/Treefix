# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("default_local_init_op")
with ops.Graph().as_default():
    # A local variable.
    v = variables.VariableV1(
        [1.0, 2.0, 3.0],
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES])

    # An entity which is initialized through a TABLE_INITIALIZER.
    w = variables.VariableV1([4, 5, 6], trainable=False, collections=[])
    ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, w.initializer)

    # This shouldn't add a variable to the VARIABLES collection responsible
    # for variables that are saved/restored from checkpoints.
    self.assertEqual(len(variables.global_variables()), 0)

    # Suppress normal variable inits to make sure the local one is
    # initialized via local_init_op.
    sv = supervisor.Supervisor(logdir=logdir, init_op=None)
    sess = sv.prepare_or_wait_for_session("")
    self.assertAllClose([1.0, 2.0, 3.0], sess.run(v))
    self.assertAllClose([4, 5, 6], sess.run(w))
    sv.stop()
