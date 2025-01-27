# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
inputs = [['a,b,c', '1,2,3', '4,5,6']]
filenames = self._setup_files(inputs)
select_cols = ['a', 'c']
_ = readers.make_csv_dataset(
    filenames, batch_size=1, select_columns=select_cols)
self.assertAllEqual(select_cols, ['a', 'c'])
