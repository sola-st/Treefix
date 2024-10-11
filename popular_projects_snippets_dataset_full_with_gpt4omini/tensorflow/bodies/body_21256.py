# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("session_config")
with ops.Graph().as_default():
    with ops.device("/cpu:1"):
        my_op = constant_op.constant([1.0])
    sv = supervisor.Supervisor(logdir=logdir)
    sess = sv.prepare_or_wait_for_session(
        "", config=config_pb2.ConfigProto(device_count={"CPU": 2}))
    for _ in range(10):
        self.evaluate(my_op)
    sess.close()
    sv.stop()
