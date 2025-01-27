# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("basics")
sw = self._FileWriter(test_dir)

sw.add_session_log(event_pb2.SessionLog(status=SessionLog.START), 1)
sw.add_summary(
    summary_pb2.Summary(
        value=[summary_pb2.Summary.Value(
            tag="mee", simple_value=10.0)]),
    10)
sw.add_summary(
    summary_pb2.Summary(
        value=[summary_pb2.Summary.Value(
            tag="boo", simple_value=20.0)]),
    20)
with ops.Graph().as_default() as g:
    constant_op.constant([0], name="zero")
sw.add_graph(g, global_step=30)

run_metadata = config_pb2.RunMetadata()
device_stats = run_metadata.step_stats.dev_stats.add()
device_stats.device = "test"
sw.add_run_metadata(run_metadata, "test run", global_step=40)
sw.close()
rr = self._EventsReader(test_dir)

# The first event should list the file_version.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)

# The next event should be the START message.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(1, ev.step)
self.assertEqual(SessionLog.START, ev.session_log.status)

# The next event should have the value 'mee=10.0'.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(10, ev.step)
self.assertProtoEquals("""
      value { tag: 'mee' simple_value: 10.0 }
      """, ev.summary)

# The next event should have the value 'boo=20.0'.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(20, ev.step)
self.assertProtoEquals("""
      value { tag: 'boo' simple_value: 20.0 }
      """, ev.summary)

# The next event should have the graph_def.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(30, ev.step)
ev_graph = graph_pb2.GraphDef()
ev_graph.ParseFromString(ev.graph_def)
self.assertProtoEquals(g.as_graph_def(add_shapes=True), ev_graph)

# The next event should have metadata for the run.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(40, ev.step)
self.assertEqual("test run", ev.tagged_run_metadata.tag)
parsed_run_metadata = config_pb2.RunMetadata()
parsed_run_metadata.ParseFromString(ev.tagged_run_metadata.run_metadata)
self.assertProtoEquals(run_metadata, parsed_run_metadata)

# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
