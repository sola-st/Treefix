# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self.get_temp_dir()
sw = self._FileWriter(test_dir)
writer_thread = sw.event_writer._worker
with test.mock.patch.object(
    writer_thread, "_ev_writer", autospec=True) as mock_writer:
    mock_writer.WriteEvent.side_effect = FakeWriteError()
    sw.add_event(event_pb2.Event())
    with self.assertRaises(FakeWriteError):
        sw.close()
