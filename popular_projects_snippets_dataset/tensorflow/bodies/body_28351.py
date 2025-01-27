# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
zlib_files = []
for i, fn in enumerate(self._filenames):
    with open(fn, "rb") as f:
        cdata = zlib.compress(f.read())

        zfn = os.path.join(self.get_temp_dir(), "tfrecord_%s.z" % i)
        with open(zfn, "wb") as f:
            f.write(cdata)
        zlib_files.append(zfn)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
dataset = self._dataset_factory(zlib_files, compression_type="ZLIB")
self.assertDatasetProduces(dataset, expected_output=expected_output)
