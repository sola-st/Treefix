# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("use_after_close")
sw = self._FileWriter(test_dir)
sw.close()
with warnings.catch_warnings(record=True) as triggered:
    warnings.simplefilter("always")
    self.assertFalse(triggered)
    sw.add_summary(summary_pb2.Summary())
    sw.add_session_log(event_pb2.SessionLog())
    sw.add_graph(ops.Graph())

self.assertEqual(len(triggered), 3)
for w in triggered:
    self.assertEqual(w.category, UserWarning)
