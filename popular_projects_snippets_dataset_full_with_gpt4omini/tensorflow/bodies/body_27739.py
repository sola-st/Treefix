# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
ds1 = dataset_ops.Dataset.range(10).window(2)
ds2 = dataset_ops.Dataset.range(10, 20).window(2)
ds = dataset_ops.Dataset.sample_from_datasets([ds1, ds2],
                                              weights=[0.3, 0.7])
ds = ds.flat_map(lambda x: x)
next_element = self.getNext(ds, requires_initialization=True)
self.evaluate(next_element())
