# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("restore_from_meta_graph")
with ops.Graph().as_default():
    variables.VariableV1(1, name="v0")
    sv = supervisor.Supervisor(logdir=logdir)
    sess = sv.prepare_or_wait_for_session("")
    filename = sv.saver.save(sess, sv.save_path)
    sv.stop()
# Create a new Graph and Supervisor and recover.
with ops.Graph().as_default():
    new_saver = saver_lib.import_meta_graph(".".join([filename, "meta"]))
    self.assertIsNotNone(new_saver)
    sv2 = supervisor.Supervisor(logdir=logdir, saver=new_saver)
    sess = sv2.prepare_or_wait_for_session("")
    self.assertEqual(1, sess.run("v0:0"))
    sv2.saver.save(sess, sv2.save_path)
    sv2.stop()
