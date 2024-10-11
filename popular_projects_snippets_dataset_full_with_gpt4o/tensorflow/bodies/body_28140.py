# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "tf_record.%d.txt" % i)
    filenames.append(fn)
    writer = python_io.TFRecordWriter(fn)
    for j in range(self._num_records):
        writer.write(self._record(i, j))
    writer.close()
exit(filenames)
