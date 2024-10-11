# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
logdir = self.get_temp_dir()
with session.Session() as sess:
    # Initial file writer
    writer1 = writer.FileWriter(session=sess, logdir=logdir)
    writer1.add_summary(self._createTaggedSummary("one"), 1)
    writer1.flush()

    # File writer, should share file with writer1
    writer2 = writer.FileWriter(session=sess, logdir=logdir)
    writer2.add_summary(self._createTaggedSummary("two"), 2)
    writer2.flush()

    # File writer with different logdir (shouldn't be in this logdir at all)
    writer3 = writer.FileWriter(session=sess, logdir=logdir + "-other")
    writer3.add_summary(self._createTaggedSummary("three"), 3)
    writer3.flush()

    # File writer in a different session (should be in separate file)
    time.sleep(1.1)  # Ensure filename has a different timestamp
    with session.Session() as other_sess:
        writer4 = writer.FileWriter(session=other_sess, logdir=logdir)
        writer4.add_summary(self._createTaggedSummary("four"), 4)
        writer4.flush()

    # One more file writer, should share file with writer1
    writer5 = writer.FileWriter(session=sess, logdir=logdir)
    writer5.add_summary(self._createTaggedSummary("five"), 5)
    writer5.flush()

event_paths = iter(sorted(glob.glob(os.path.join(logdir, "event*"))))

# First file should have tags "one", "two", and "five"
events = summary_iterator.summary_iterator(next(event_paths))
self.assertEqual("brain.Event:2", next(events).file_version)
self.assertEqual("one", next(events).summary.value[0].tag)
self.assertEqual("two", next(events).summary.value[0].tag)
self.assertEqual("five", next(events).summary.value[0].tag)
self.assertRaises(StopIteration, lambda: next(events))

# Second file should have just "four"
events = summary_iterator.summary_iterator(next(event_paths))
self.assertEqual("brain.Event:2", next(events).file_version)
self.assertEqual("four", next(events).summary.value[0].tag)
self.assertRaises(StopIteration, lambda: next(events))

# No more files
self.assertRaises(StopIteration, lambda: next(event_paths))

# Just check that the other logdir file exists to be sure we wrote it
self.assertTrue(glob.glob(os.path.join(logdir + "-other", "event*")))
