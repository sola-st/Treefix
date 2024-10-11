# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
with ops.device("cpu:0"):
    repeat_count = variables.Variable(constant_op.constant(10, dtypes.int64))
    dataset = dataset_ops.Dataset.range(3).flat_map(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(repeat_count))

    options = options_lib.Options()
    options.experimental_optimization.inject_prefetch = False
    dataset = dataset.with_options(options)

    cached_dataset = dataset.cache().repeat(2)
    uncached_dataset = dataset.repeat(2)

    self.evaluate(repeat_count.initializer)
    # Needs to be initializable to capture the variable.
    cached_next = self.getNext(cached_dataset, requires_initialization=True)
    uncached_next = self.getNext(
        uncached_dataset, requires_initialization=True)
    for i in range(3):
        for _ in range(10):
            self.assertEqual(self.evaluate(cached_next()), i)
            self.assertEqual(self.evaluate(uncached_next()), i)

    self.evaluate(repeat_count.assign(0))

    # The uncached iterator should now be empty.
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(uncached_next())

    # The cached iterator replays from cache.
    for i in range(3):
        for _ in range(10):
            self.assertEqual(self.evaluate(cached_next()), i)

      # The cached iterator should now be empty.
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(cached_next())
