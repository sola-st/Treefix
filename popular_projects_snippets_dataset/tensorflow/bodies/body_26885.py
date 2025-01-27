# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sleep_test.py
self.skipTest("b/123597912")
sleep_microseconds = 100
dataset = dataset_ops.Dataset.range(10).apply(
    testing.sleep(sleep_microseconds))
next_element = self.getNext(dataset)
start_time = time.time()
for i in range(10):
    self.assertEqual(i, self.evaluate(next_element()))
end_time = time.time()
self.assertGreater(end_time - start_time, (10 * sleep_microseconds) / 1e6)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
