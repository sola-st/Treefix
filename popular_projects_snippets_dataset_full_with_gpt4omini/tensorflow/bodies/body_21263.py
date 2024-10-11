# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("explicit_summary_writer")
with ops.Graph().as_default():
    summary.scalar("c1", constant_op.constant(1))
    summary.scalar("c2", constant_op.constant(2))
    summary.scalar("c3", constant_op.constant(3))
    summ = summary.merge_all()
    sw = writer.FileWriter(logdir)
    sv = supervisor.Supervisor(logdir="", summary_op=None, summary_writer=sw)
    meta_graph_def = meta_graph.create_meta_graph_def()
    sess = sv.prepare_or_wait_for_session("")
    sv.summary_computed(sess, sess.run(summ))
    sess.close()
    # Wait to make sure everything is written to file before stopping.
    time.sleep(1)
    sv.stop()

# Check the summary was written to 'logdir'
rr = _summary_iterator(logdir)

# The first event should list the file_version.
ev = next(rr)
self.assertEqual("brain.Event:2", ev.file_version)

# The next one has the graph.
ev = next(rr)
ev_graph = graph_pb2.GraphDef()
ev_graph.ParseFromString(ev.graph_def)
self.assertProtoEquals(sess.graph.as_graph_def(add_shapes=True), ev_graph)

# Stored MetaGraphDef
ev = next(rr)
ev_meta_graph = meta_graph_pb2.MetaGraphDef()
ev_meta_graph.ParseFromString(ev.meta_graph_def)
self.assertProtoEquals(meta_graph_def, ev_meta_graph)
self.assertProtoEquals(
    sess.graph.as_graph_def(add_shapes=True), ev_meta_graph.graph_def)

# The next one should have the values from the summary.
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
self.assertRaises(StopIteration, lambda: next(rr))
