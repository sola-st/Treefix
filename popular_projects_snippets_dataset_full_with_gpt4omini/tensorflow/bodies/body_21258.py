# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default():
    sv = supervisor.Supervisor(is_chief=False)
    sess = sv.prepare_or_wait_for_session("")
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summ = summary.merge_all()
    sv.summary_computed(sess, sess.run(summ))
