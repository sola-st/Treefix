# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_iterator_test.py
test_dir = os.path.join(self.get_temp_dir(), "events")
with writer.FileWriter(test_dir) as w:
    session_log_start = event_pb2.SessionLog.START
    w.add_session_log(event_pb2.SessionLog(status=session_log_start), 1)
    w.flush()
    path = glob.glob(os.path.join(test_dir, "event*"))[0]
    rr = summary_iterator.summary_iterator(path)
    # The first event should list the file_version.
    ev = next(rr)
    self.assertEqual("brain.Event:2", ev.file_version)
    # The next event should be the START message.
    ev = next(rr)
    self.assertEqual(1, ev.step)
    self.assertEqual(session_log_start, ev.session_log.status)
    # Reached EOF.
    self.assertRaises(StopIteration, lambda: next(rr))
    w.add_session_log(event_pb2.SessionLog(status=session_log_start), 2)
    w.flush()
    # The new event is read, after previously seeing EOF.
    ev = next(rr)
    self.assertEqual(2, ev.step)
    self.assertEqual(session_log_start, ev.session_log.status)
    # Get EOF again.
    self.assertRaises(StopIteration, lambda: next(rr))
