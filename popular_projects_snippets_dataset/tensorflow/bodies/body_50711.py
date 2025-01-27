# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self.get_temp_dir()
sw = self._FileWriter(test_dir)
writer_thread = sw.event_writer._worker
with test.mock.patch.object(
    writer_thread, "_ev_writer", autospec=True) as mock_writer:
    # Coordinate threads to ensure both events are added before the writer
    # thread dies, to avoid the second add_event() failing instead of flush().
    second_event_added = threading.Event()
    def _FakeWriteEvent(event):
        del event  # unused
        second_event_added.wait()
        raise FakeWriteError()
    mock_writer.WriteEvent.side_effect = _FakeWriteEvent
    sw.add_event(event_pb2.Event())
    sw.add_event(event_pb2.Event())
    second_event_added.set()
    with self.assertRaises(FakeWriteError):
        sw.flush()
