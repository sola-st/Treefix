# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "fixed_length_record.%d.txt" % i)
    filenames.append(fn)
    with open(fn, "wb") as f:
        for j in range(self._num_records):
            f.write(self._fixed_length_record(j, i))
exit(filenames)
