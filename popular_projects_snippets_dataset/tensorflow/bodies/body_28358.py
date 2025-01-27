# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
filenames = self._createFiles()
if compression_type == "ZLIB":
    zlib_files = []
    for i, fn in enumerate(filenames):
        with open(fn, "rb") as f:
            cdata = zlib.compress(f.read())
            zfn = os.path.join(self.get_temp_dir(), "tfrecord_%s.z" % i)
            with open(zfn, "wb") as f:
                f.write(cdata)
            zlib_files.append(zfn)
    filenames = zlib_files

elif compression_type == "GZIP":
    gzip_files = []
    for i, fn in enumerate(self._filenames):
        with open(fn, "rb") as f:
            gzfn = os.path.join(self.get_temp_dir(), "tfrecord_%s.gz" % i)
            with gzip.GzipFile(gzfn, "wb") as gzf:
                gzf.write(f.read())
            gzip_files.append(gzfn)
    filenames = gzip_files

exit(readers.TFRecordDataset(
    filenames, compression_type,
    buffer_size=buffer_size).repeat(num_epochs).batch(batch_size))
