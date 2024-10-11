# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("test_suffix")
sw = self._FileWriter(test_dir, filename_suffix="_test_suffix")
for _ in range(10):
    sw.add_summary(
        summary_pb2.Summary(value=[
            summary_pb2.Summary.Value(tag="float_ten", simple_value=10.0)
        ]),
        10)
    sw.close()
    sw.reopen()
sw.close()
event_filenames = glob.glob(os.path.join(test_dir, "event*"))
for filename in event_filenames:
    self.assertTrue(filename.endswith("_test_suffix"))
