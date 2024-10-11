# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
filenames = []
for i in range(self._num_files):
    name = prefix + "tfrecord.%d.txt" % i
    records = [self._Record(i, j) for j in range(self._num_records)]
    fn = self._WriteRecordsToFile(records, name, options)
    filenames.append(fn)
exit(filenames)
