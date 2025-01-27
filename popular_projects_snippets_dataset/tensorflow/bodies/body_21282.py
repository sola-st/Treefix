# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("standard_services_with_global_step")
# Create a checkpoint.
with ops.Graph().as_default():
    v = variables.VariableV1([123], name="global_step")
    sv = supervisor.Supervisor(logdir=logdir)
    meta_graph_def = meta_graph.create_meta_graph_def(
        saver_def=sv.saver.saver_def)
    sess = sv.prepare_or_wait_for_session("")
    # This is where the checkpoint will appear, with step number 123.
    save_path = "%s-123" % sv.save_path
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
ev = next(rr)
ev_meta_graph = meta_graph_pb2.MetaGraphDef()
ev_meta_graph.ParseFromString(ev.meta_graph_def)
self.assertProtoEquals(meta_graph_def, ev_meta_graph)
self.assertProtoEquals(
    sess.graph.as_graph_def(add_shapes=True), ev_meta_graph.graph_def)
ev = next(rr)
# It is actually undeterministic whether SessionLog.START gets written
# before the summary or the checkpoint, but this works when run 10000 times.
self.assertEqual(123, ev.step)
self.assertEqual(event_pb2.SessionLog.START, ev.session_log.status)
first = next(rr)
second = next(rr)
# It is undeterministic whether the value gets written before the checkpoint
# since they are on separate threads, so we check for both conditions.
if first.HasField("summary"):
    self.assertProtoEquals("""value { tag: 'global_step/sec'
                                        simple_value: 0.0 }""", first.summary)
    self.assertEqual(123, second.step)
    self.assertEqual(event_pb2.SessionLog.CHECKPOINT,
                     second.session_log.status)
else:
    self.assertEqual(123, first.step)
    self.assertEqual(event_pb2.SessionLog.CHECKPOINT,
                     first.session_log.status)
    self.assertProtoEquals("""value { tag: 'global_step/sec'
                                        simple_value: 0.0 }""", second.summary)
ev = next(rr)
self.assertEqual(event_pb2.SessionLog.STOP, ev.session_log.status)
self.assertRaises(StopIteration, lambda: next(rr))
# There should be a checkpoint file with the variable "foo"
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1([-12], name="global_step")
    sav = saver_lib.Saver([v])
    sav.restore(sess, save_path)
    self.assertEqual(123, self.evaluate(v)[0])
