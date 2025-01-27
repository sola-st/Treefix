# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
with context.execution_mode(execution_mode):
    val = 0
    dataset = dataset_ops.Dataset.range(10)
    for foo in dataset:
        self.assertEqual(val, foo.numpy())
        val += 1
