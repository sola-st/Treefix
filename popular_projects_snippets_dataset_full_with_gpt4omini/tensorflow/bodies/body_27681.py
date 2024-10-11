# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
verify_fn(self, lambda: self._build_ds(cycle_length, block_length),
          self.num_outputs)
