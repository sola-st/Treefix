# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 3
inputs = [['1,"2"3",4', '1,"2"3",4",5,5', 'a,b,"c"d"', 'e,f,g']]
filenames = self._setup_files(inputs)
dataset = readers.CsvDataset(filenames, record_defaults=record_defaults)
dataset = dataset.apply(error_ops.ignore_errors())
self.assertDatasetProduces(dataset, [(b'e', b'f', b'g')])
