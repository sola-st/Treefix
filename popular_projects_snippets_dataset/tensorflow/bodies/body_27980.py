# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
dataset = make_dataset(nrows)

# Get the unbatched rows (so we can check expected values).
get_next = self.getNext(dataset)
rows = [nest.map_structure(_to_list, self.evaluate(get_next()))
        for _ in range(nrows)]

# Batch the dataset, and check that batches match slices from `rows`.
batched_dataset = dataset.ragged_batch(batch_size, drop_remainder)
get_next = self.getNext(batched_dataset)
for start_row in range(0, nrows, batch_size):
    end_row = start_row + batch_size
    if end_row > nrows and drop_remainder:
        break
    end_row = min(end_row, nrows)
    result = self.evaluate(get_next())

    # Use nest for potentially nested datasets.
    nest.map_structure_up_to(
        result, lambda a, *b: self.assertAllEqual(a, list(b)),
        result, *rows[start_row:end_row])

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
