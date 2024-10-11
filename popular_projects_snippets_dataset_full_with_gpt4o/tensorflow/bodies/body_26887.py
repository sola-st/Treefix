# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sleep_test.py
ds = dataset_ops.Dataset.range(1)

sleep_microseconds = int(1e6) * 1000
ds_sleep = dataset_ops.Dataset.range(1)
ds_sleep = ds.apply(testing.sleep(sleep_microseconds))

ds = ds.concatenate(ds_sleep)
ds = ds.prefetch(1)

get_next = self.getNext(ds, requires_initialization=True)

with self.cached_session():
    self.assertEqual(self.evaluate(get_next()), 0)
