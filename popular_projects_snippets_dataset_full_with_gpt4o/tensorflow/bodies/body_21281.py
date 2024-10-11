# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("standard_services_without_global_step")
# Create a checkpoint.
with ops.Graph().as_default():
    v = variables.VariableV1([1.0], name="foo")
    summary.scalar("v", v[0])
    sv = supervisor.Supervisor(logdir=logdir)
    meta_graph_def = meta_graph.create_meta_graph_def(
        saver_def=sv.saver.saver_def)
    sess = sv.prepare_or_wait_for_session("")
    save_path = sv.save_path
    self._wait_for_glob(save_path, 3.0)
    self._wait_for_glob(
        os.path.join(logdir, "*events*"), 3.0, for_checkpoint=False)
    # Wait to make sure everything is written to file before stopping.
    time.sleep(1)
    sv.stop()
# There should be an event file with a version number.
rr = _summary_iterator(logdir)
ev = next(rr)
self.assertEqual("brain.Event:2", ev.file_version)
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

ev = next(rr)
self.assertProtoEquals("value { tag: 'v' simple_value: 1.0 }", ev.summary)

ev = next(rr)
self.assertEqual(event_pb2.SessionLog.STOP, ev.session_log.status)

self.assertRaises(StopIteration, lambda: next(rr))
# There should be a checkpoint file with the variable "foo"
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1([10.10], name="foo")
    sav = saver_lib.Saver([v])
    sav.restore(sess, save_path)
    self.assertEqual(1.0, self.evaluate(v)[0])
