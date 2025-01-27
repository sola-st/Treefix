# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("managed_keep_summary_writer")
with ops.Graph().as_default():
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summary.scalar("c3", constant_op.constant(3))
    summ = summary.merge_all()
    sv = supervisor.Supervisor(logdir=logdir)
    with sv.managed_session(
        "", close_summary_writer=False,
        start_standard_services=False) as sess:
        sv.summary_computed(sess, sess.run(summ))
    with sv.managed_session(
        "", close_summary_writer=False,
        start_standard_services=False) as sess:
        sv.summary_computed(sess, sess.run(summ))
    # Now close the summary writer to flush the events.
sv.summary_writer.close()
# The summary iterator should report the summary twice as we reused
# the same summary writer across the 2 sessions.
rr = _summary_iterator(logdir)
# The first event should list the file_version.
ev = next(rr)
self.assertEqual("brain.Event:2", ev.file_version)

# The next one has the graph.
ev = next(rr)
self.assertTrue(ev.graph_def)

ev = next(rr)
self.assertTrue(ev.meta_graph_def)

# The next one should have the values from the summary.
ev = next(rr)
self.assertProtoEquals("""
      value { tag: 'c1' simple_value: 1.0 }
      value { tag: 'c2' simple_value: 2.0 }
      value { tag: 'c3' simple_value: 3.0 }
      """, ev.summary)

# The next one should also have the values from the summary.
ev = next(rr)
self.assertProtoEquals("""
      value { tag: 'c1' simple_value: 1.0 }
      value { tag: 'c2' simple_value: 2.0 }
      value { tag: 'c3' simple_value: 3.0 }
      """, ev.summary)

# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
