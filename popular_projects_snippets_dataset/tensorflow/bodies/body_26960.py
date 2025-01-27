# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
super(CsvDatasetCheckpointTest, self).setUp()
self._num_cols = 7
self._num_rows = 10
self._num_epochs = 14
self._num_outputs = self._num_rows * self._num_epochs

inputs = [
    ','.join(str(self._num_cols * j + i)
             for i in range(self._num_cols))
    for j in range(self._num_rows)
]
contents = '\n'.join(inputs).encode('utf-8')

self._filename = os.path.join(self.get_temp_dir(), 'file.csv')
self._compressed = os.path.join(self.get_temp_dir(),
                                'comp.csv')  # GZip compressed

with open(self._filename, 'wb') as f:
    f.write(contents)
with gzip.GzipFile(self._compressed, 'wb') as f:
    f.write(contents)
