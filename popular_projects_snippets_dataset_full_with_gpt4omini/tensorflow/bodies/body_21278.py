# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("setup_fail")
with ops.Graph().as_default():
    variables.VariableV1([1.0, 2.0, 3.0], name="v")
    with self.assertRaisesRegex(ValueError, "must have their device set"):
        supervisor.Supervisor(logdir=logdir, is_chief=False)
with ops.Graph().as_default(), ops.device("/job:ps"):
    variables.VariableV1([1.0, 2.0, 3.0], name="v")
    supervisor.Supervisor(logdir=logdir, is_chief=False)
