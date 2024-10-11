# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
gzip_files = []
for i, fn in enumerate(self._filenames):
    with open(fn, "rb") as f:
        gzfn = os.path.join(self.get_temp_dir(), "tfrecord_%s.gz" % i)
        with gzip.GzipFile(gzfn, "wb") as gzf:
            gzf.write(f.read())
        gzip_files.append(gzfn)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
dataset = self._dataset_factory(gzip_files, compression_type="GZIP")
self.assertDatasetProduces(dataset, expected_output=expected_output)
