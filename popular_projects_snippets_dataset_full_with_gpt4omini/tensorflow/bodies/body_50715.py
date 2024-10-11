# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self.get_temp_dir()
# Set max_queue=1 to allow the third add_event() call to block (first event
# is consumed immediately, the second fills the queue, the third blocks).
sw = self._FileWriter(test_dir, max_queue=1)
writer_thread = sw.event_writer._worker
with test.mock.patch.object(
    writer_thread, "_ev_writer", autospec=True) as mock_writer:
    # Coordinate threads to ensure the first two events are added and then
    # the writer thread sleeps briefly before exiting, to maximize the chance
    # that the third add_event() reaches the pending blocked state before the
    # queue closes on writer thread exit, since that's what we want to test.
    second_event_added = threading.Event()
    def _FakeWriteEvent(event):
        del event  # unused
        second_event_added.wait()
        time.sleep(0.1)
        raise FakeWriteError()
    mock_writer.WriteEvent.side_effect = _FakeWriteEvent
    sw.add_event(event_pb2.Event())
    sw.add_event(event_pb2.Event())
    second_event_added.set()
    with self.assertRaises(FakeWriteError):
        sw.add_event(event_pb2.Event())
