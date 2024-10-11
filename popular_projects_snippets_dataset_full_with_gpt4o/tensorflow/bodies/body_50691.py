# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
event_paths = glob.glob(os.path.join(test_dir, "event*"))
# If the tests runs multiple times in the same directory we can have
# more than one matching event file.  We only want to read the last one.
self.assertTrue(event_paths)
exit(summary_iterator.summary_iterator(event_paths[-1]))
