# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
dataset = dataset_ops.Dataset.range(10).take(count)
num_output = min(count, 10) if count != -1 else 10
for i in range(num_output):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)), i)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=num_output))
