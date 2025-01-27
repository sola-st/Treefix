# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("managed_not_keep_summary_writer")
with ops.Graph().as_default():
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summary.scalar("c3", constant_op.constant(3))
    summ = summary.merge_all()
    sv = supervisor.Supervisor(logdir=logdir, summary_op=None)
    with sv.managed_session(
        "", close_summary_writer=True, start_standard_services=False) as sess:
        sv.summary_computed(sess, sess.run(summ))
    # Sleep 1.2s to make sure that the next event file has a different name
    # than the current one.
    time.sleep(1.2)
    with sv.managed_session(
        "", close_summary_writer=True, start_standard_services=False) as sess:
        sv.summary_computed(sess, sess.run(summ))
event_paths = sorted(glob.glob(os.path.join(logdir, "event*")))
self.assertEqual(2, len(event_paths))
# The two event files should have the same contents.
for path in event_paths:
    # The summary iterator should report the summary once as we closed the
    # summary writer across the 2 sessions.
    rr = summary_iterator.summary_iterator(path)
    # The first event should list the file_version.
    ev = next(rr)
    self.assertEqual("brain.Event:2", ev.file_version)

    # The next one has the graph and metagraph.
    ev = next(rr)
    self.assertTrue(ev.graph_def)

    ev = next(rr)
    self.assertTrue(ev.meta_graph_def)

    # The next one should have the values from the summary.
    # But only once.
    ev = next(rr)
    self.assertProtoEquals("""
        value { tag: 'c1' simple_value: 1.0 }
        value { tag: 'c2' simple_value: 2.0 }
        value { tag: 'c3' simple_value: 3.0 }
        """, ev.summary)

    # The next one should be a stop message if we closed cleanly.
    ev = next(rr)
    self.assertEqual(event_pb2.SessionLog.STOP, ev.session_log.status)

    # We should be done.
    with self.assertRaises(StopIteration):
        next(rr)
