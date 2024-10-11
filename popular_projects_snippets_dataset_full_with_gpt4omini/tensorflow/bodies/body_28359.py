# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
num_epochs = 5
num_outputs = num_epochs * self._num_files * self._num_records // batch_size
verify_fn(self,
          lambda: self.make_dataset(num_epochs, batch_size=batch_size),
          num_outputs)
