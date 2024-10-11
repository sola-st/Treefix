# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
defs = [[0]] * self._num_cols
verify_fn(self, lambda: self.ds_func(record_defaults=defs, buffer_size=2),
          self._num_outputs)
