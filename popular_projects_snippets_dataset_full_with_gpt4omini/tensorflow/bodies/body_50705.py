# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("global_step")
sw = self._FileWriter(test_dir)
with self.cached_session():
    i = constant_op.constant(1, dtype=dtypes.int32, shape=[])
    l = constant_op.constant(2, dtype=dtypes.int64, shape=[])
    # Test the summary can be passed serialized.
    summ = summary_pb2.Summary(
        value=[summary_pb2.Summary.Value(
            tag="i", simple_value=1.0)])
    sw.add_summary(summ.SerializeToString(), self.evaluate(i))
    sw.add_summary(
        summary_pb2.Summary(
            value=[summary_pb2.Summary.Value(tag="l", simple_value=2.0)]),
        self.evaluate(l))
    sw.close()

rr = self._EventsReader(test_dir)

# File_version.
ev = next(rr)
self.assertTrue(ev)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)

# Summary passed serialized.
ev = next(rr)
self.assertTrue(ev)
self.assertRecent(ev.wall_time)
self.assertEqual(1, ev.step)
self.assertProtoEquals("""
      value { tag: 'i' simple_value: 1.0 }
      """, ev.summary)

# Summary passed as SummaryObject.
ev = next(rr)
self.assertTrue(ev)
self.assertRecent(ev.wall_time)
self.assertEqual(2, ev.step)
self.assertProtoEquals("""
      value { tag: 'l' simple_value: 2.0 }
      """, ev.summary)

# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
