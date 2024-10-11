# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
with context.eager_mode(), context.execution_mode(execution_mode):
    val = 0
    dataset = dataset_ops.Dataset.range(10)
    iterator = iter(dataset)
    for foo in iterator:
        self.assertEqual(val, foo.numpy())
        val += 1
