# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default():
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summary.scalar("c3", constant_op.constant(3))
    summ = summary.merge_all()
    sv = supervisor.Supervisor(logdir="", summary_op=None)
    sess = sv.prepare_or_wait_for_session("")
    with self.assertRaisesRegex(RuntimeError, "requires a summary writer"):
        sv.summary_computed(sess, sess.run(summ))
