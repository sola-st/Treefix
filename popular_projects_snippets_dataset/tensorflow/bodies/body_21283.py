# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    sv = supervisor.Supervisor(logdir=self._test_dir("no_queue_runners"))
    self.assertEqual(0, len(sv.start_queue_runners(sess)))
    sv.stop()
