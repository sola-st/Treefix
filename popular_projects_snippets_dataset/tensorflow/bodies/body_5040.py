# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
next_element_fn = self._getNext(dataset)
with self.cached_session():
    for f in range(self._shard_index, self._num_files, self._num_shards):
        for r in range(self._num_records):
            self.assertAllEqual(record_fn(r, f), self.evaluate(next_element_fn()))
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element_fn())
