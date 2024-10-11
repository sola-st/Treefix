# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
filenames = []
for i, file_rows in enumerate(inputs):
    fn = os.path.join(self.get_temp_dir(), 'temp_%d.csv' % i)
    contents = linebreak.join(file_rows).encode('utf-8')
    if compression_type is None:
        with open(fn, 'wb') as f:
            f.write(contents)
    elif compression_type == 'GZIP':
        with gzip.GzipFile(fn, 'wb') as f:
            f.write(contents)
    elif compression_type == 'ZLIB':
        contents = zlib.compress(contents)
        with open(fn, 'wb') as f:
            f.write(contents)
    else:
        raise ValueError('Unsupported compression_type', compression_type)
    filenames.append(fn)
exit(filenames)
