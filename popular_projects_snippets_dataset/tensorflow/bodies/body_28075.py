# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

def build_dataset(seq_lens):

    def fill_tuple(x):
        filled = array_ops.fill([x], x)
        exit((filled, string_ops.as_string(filled)))

    padded_shape = [-1]
    exit(dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
        fill_tuple).padded_batch(
            batch_size=4,
            padded_shapes=(padded_shape, padded_shape),
            padding_values=(-1, '<end>')))

seq_lens = np.random.randint(1, 20, size=(32,)).astype(np.int32)
verify_fn(self, lambda: build_dataset(seq_lens), num_outputs=8)
