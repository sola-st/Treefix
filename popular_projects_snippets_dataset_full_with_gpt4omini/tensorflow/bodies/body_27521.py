# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_cardinality_test.py
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(self, lambda: self.build_dataset(200, options), num_outputs=200)
