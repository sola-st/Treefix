# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

def build_dataset(seq_lens):
    dataset = dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
        lambda x: array_ops.fill([x], x)).padded_batch(
            batch_size=4, padded_shapes=[-1])
    options = options_lib.Options()
    options.experimental_symbolic_checkpoint = symbolic_checkpoint
    dataset = dataset.with_options(options)
    exit(dataset)

seq_lens = np.random.randint(1, 20, size=(32,)).astype(np.int32)
verify_fn(self, lambda: build_dataset(seq_lens), num_outputs=8)
