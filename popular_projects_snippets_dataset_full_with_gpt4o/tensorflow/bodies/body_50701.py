# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("close_and_reopen")
sw = self._FileWriter(test_dir)
sw.add_session_log(event_pb2.SessionLog(status=SessionLog.START), 1)
sw.close()
# Sleep at least one second to make sure we get a new event file name.
time.sleep(1.2)
sw.reopen()
sw.add_session_log(event_pb2.SessionLog(status=SessionLog.START), 2)
sw.close()

# We should now have 2 events files.
event_paths = sorted(glob.glob(os.path.join(test_dir, "event*")))
self.assertEqual(2, len(event_paths))

# Check the first file contents.
rr = summary_iterator.summary_iterator(event_paths[0])
# The first event should list the file_version.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)
# The next event should be the START message.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(1, ev.step)
self.assertEqual(SessionLog.START, ev.session_log.status)
# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))

# Check the second file contents.
rr = summary_iterator.summary_iterator(event_paths[1])
# The first event should list the file_version.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)
# The next event should be the START message.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(2, ev.step)
self.assertEqual(SessionLog.START, ev.session_log.status)
# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
