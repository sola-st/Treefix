# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("basics")
sw = self._FileWriter(test_dir)

sw.add_session_log(event_pb2.SessionLog(status=SessionLog.START), 1)

# We add 2 summaries with the same tags. They both have metadata. The writer
# should strip the metadata from the second one.
value = summary_pb2.Summary.Value(tag="foo", simple_value=10.0)
value.metadata.plugin_data.plugin_name = "bar"
value.metadata.plugin_data.content = compat.as_bytes("... content ...")
sw.add_summary(summary_pb2.Summary(value=[value]), 10)
value = summary_pb2.Summary.Value(tag="foo", simple_value=10.0)
value.metadata.plugin_data.plugin_name = "bar"
value.metadata.plugin_data.content = compat.as_bytes("... content ...")
sw.add_summary(summary_pb2.Summary(value=[value]), 10)

sw.close()
rr = self._EventsReader(test_dir)

# The first event should list the file_version.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)

# The next event should be the START message.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(1, ev.step)
self.assertEqual(SessionLog.START, ev.session_log.status)

# This is the first event with tag foo. It should contain SummaryMetadata.
ev = next(rr)
self.assertProtoEquals("""
      value {
        tag: "foo"
        simple_value: 10.0
        metadata {
          plugin_data {
            plugin_name: "bar"
            content: "... content ..."
          }
        }
      }
      """, ev.summary)

# This is the second event with tag foo. It should lack SummaryMetadata
# because the file writer should have stripped it.
ev = next(rr)
self.assertProtoEquals("""
      value {
        tag: "foo"
        simple_value: 10.0
      }
      """, ev.summary)

# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
