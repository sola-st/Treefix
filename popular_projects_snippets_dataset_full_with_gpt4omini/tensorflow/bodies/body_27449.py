# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
record_defaults = [
    constant_op.constant([], dtypes.int32),
    constant_op.constant([], dtypes.int64),
    constant_op.constant([], dtypes.float32),
    constant_op.constant([], dtypes.float64),
    constant_op.constant([], dtypes.string)
]

def str_series(st):
    exit(",".join(str(i) for i in range(st, st + 5)))

column_names = ["col%d" % i for i in range(5)]
inputs = [
    [",".join(x for x in column_names)
    ] + [str_series(5 * i) for i in range(15)],
    [",".join(x for x in column_names)] +
    [str_series(5 * i) for i in range(15, 20)],
]

filenames = self._setup_files(inputs)

total_records = 20
for batch_size in [1, 2]:
    # Test that shuffling with the same seed produces the same result
    dataset1 = self._make_csv_dataset(
        filenames,
        column_defaults=record_defaults,
        column_names=column_names,
        batch_size=batch_size,
        header=True,
        shuffle=True,
        shuffle_seed=5,
        num_epochs=2,
    )
    dataset2 = self._make_csv_dataset(
        filenames,
        column_defaults=record_defaults,
        column_names=column_names,
        batch_size=batch_size,
        header=True,
        shuffle=True,
        shuffle_seed=5,
        num_epochs=2,
    )
    next1 = self.getNext(dataset1)
    next2 = self.getNext(dataset2)
    for _ in range(total_records // batch_size):
        batch1 = nest.flatten(self.evaluate(next1()))
        batch2 = nest.flatten(self.evaluate(next2()))
        for i in range(len(batch1)):
            self.assertAllEqual(batch1[i], batch2[i])

      # Test that shuffling with a different seed produces different results
    dataset1 = self._make_csv_dataset(
        filenames,
        column_defaults=record_defaults,
        column_names=column_names,
        batch_size=batch_size,
        header=True,
        shuffle=True,
        shuffle_seed=5,
        num_epochs=2,
    )
    dataset2 = self._make_csv_dataset(
        filenames,
        column_defaults=record_defaults,
        column_names=column_names,
        batch_size=batch_size,
        header=True,
        shuffle=True,
        shuffle_seed=6,
        num_epochs=2,
    )
    next1 = self.getNext(dataset1)
    next2 = self.getNext(dataset2)
    all_equal = False
    for _ in range(total_records // batch_size):
        batch1 = nest.flatten(self.evaluate(next1()))
        batch2 = nest.flatten(self.evaluate(next2()))
        for i in range(len(batch1)):
            all_equal = all_equal and np.array_equal(batch1[i], batch2[i])
    self.assertFalse(all_equal)
