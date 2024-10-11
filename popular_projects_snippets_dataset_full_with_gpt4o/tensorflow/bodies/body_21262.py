# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("explicit_no_summary_writer")
with ops.Graph().as_default():
    variables.VariableV1([1.0], name="foo")
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summary.scalar("c3", constant_op.constant(3))
    summ = summary.merge_all()
    sv = supervisor.Supervisor(logdir=logdir, summary_writer=None)
    sess = sv.prepare_or_wait_for_session("")
    # Check that a checkpoint is still be generated.
    self._wait_for_glob(sv.save_path, 3.0)
    # Check that we cannot write a summary
    with self.assertRaisesRegex(RuntimeError, "requires a summary writer"):
        sv.summary_computed(sess, sess.run(summ))
