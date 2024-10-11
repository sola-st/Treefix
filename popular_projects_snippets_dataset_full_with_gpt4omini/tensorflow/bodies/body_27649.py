# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
seed = 42
num_elements_per_file = 8
num_files = 3
num_epochs = 2
num_outputs = num_elements_per_file * num_files * num_epochs
# pylint: disable=g-long-lambda
verify_fn(
    self, lambda: self._build_dataset(
        num_elements_per_file=num_elements_per_file,
        num_files=num_files,
        num_epochs=num_epochs,
        seed=seed,
        reshuffle_each_iteration=reshuffle_each_iteration,
        symbolic_checkpoint=symbolic_checkpoint), num_outputs)
