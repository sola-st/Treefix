# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
range_dataset = dataset_ops.Dataset.range(42)
dict_dataset = dataset_ops.Dataset.from_tensor_slices({"a": [1, 2],
                                                       "b": [3, 4]})
tuple_dataset = dataset_ops.Dataset.from_tensor_slices(([1, 2], [3, 4]))
dataset = dataset_ops.Dataset.zip((range_dataset, dict_dataset,
                                   tuple_dataset))
io.save(dataset, self._test_dir)
dataset_loaded = io.load(self._test_dir)
self.assertDatasetsEqual(dataset, dataset_loaded)
