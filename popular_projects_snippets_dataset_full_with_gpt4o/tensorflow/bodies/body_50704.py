# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("with_statement")
with self._FileWriter(test_dir) as sw:
    sw.add_session_log(event_pb2.SessionLog(status=SessionLog.START), 1)
event_paths = sorted(glob.glob(os.path.join(test_dir, "event*")))
self.assertEqual(1, len(event_paths))
