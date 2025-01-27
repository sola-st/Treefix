# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "tf_record.%d.txt" % i)
    filenames.append(fn)
    writer = python_io.TFRecordWriter(fn)
    for j in range(self._num_records):
        record = self._record(j, i)
        writer.write(record)
    writer.close()
exit(filenames)
