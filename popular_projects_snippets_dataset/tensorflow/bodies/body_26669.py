# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/csv_dataset_benchmark.py
# Since this isn't test.TestCase, have to manually create a test dir
gfile.MakeDirs(googletest.GetTempDir())
self._temp_dir = tempfile.mkdtemp(dir=googletest.GetTempDir())

self._num_cols = [4, 64, 256]
self._num_per_iter = 5000
self._filenames = []
for n in self._num_cols:
    fn = os.path.join(self._temp_dir, 'file%d.csv' % n)
    with open(fn, 'w') as f:
        # Just write 100 rows and use `repeat`... Assumes the cost
        # of creating an iterator is not significant
        row = ','.join(str_val for _ in range(n))
        f.write('\n'.join(row for _ in range(100)))
    self._filenames.append(fn)
