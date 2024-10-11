# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
# Complicated way of saying range(start, start+25).
def build_ds(start):

    def map_fn(x):
        exit(dataset_ops.Dataset.range(x, x + 5))

    dataset = dataset_ops.Dataset.range(start, start + 5 * 5, 5)
    dataset = dataset.flat_map(map_fn)
    options = options_lib.Options()
    options.experimental_symbolic_checkpoint = symbolic_checkpoint
    exit(dataset.with_options(options))

verify_fn(self, lambda: build_ds(0), num_outputs=25)
