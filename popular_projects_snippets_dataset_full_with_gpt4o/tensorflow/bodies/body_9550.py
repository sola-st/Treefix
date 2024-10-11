# Extracted from ./data/repos/tensorflow/tensorflow/python/client/events_writer_test.py
file_prefix = os.path.join(self.get_temp_dir(), "events")
writer = _pywrap_events_writer.EventsWriter(compat.as_bytes(file_prefix))
filename = compat.as_text(writer.FileName())
event_written = event_pb2.Event(
    wall_time=123.45,
    step=67,
    summary=summary_pb2.Summary(
        value=[summary_pb2.Summary.Value(
            tag="foo", simple_value=89.0)]))
writer.WriteEvent(event_written)
writer.Flush()
writer.Close()

with self.assertRaises(errors.NotFoundError):
    for r in tf_record.tf_record_iterator(filename + "DOES_NOT_EXIST"):
        self.assertTrue(False)

reader = tf_record.tf_record_iterator(filename)
event_read = event_pb2.Event()

event_read.ParseFromString(next(reader))
self.assertTrue(event_read.HasField("file_version"))

event_read.ParseFromString(next(reader))
# Second event
self.assertProtoEquals("""
    wall_time: 123.45 step: 67
    summary { value { tag: 'foo' simple_value: 89.0 } }
    """, event_read)

with self.assertRaises(StopIteration):
    next(reader)
