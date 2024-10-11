# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

num_repeats = 2
input_values = np.array([2, 3], dtype=np.int64)

def _build_dataset():
    dataset = dataset_ops.Dataset.from_tensor_slices(input_values)
    dataset = dataset.repeat(num_repeats)
    dataset = dataset.interleave(
        lambda x: dataset_ops.Dataset.from_tensors(x).repeat(x), cycle_length,
        block_length, num_parallel_calls)
    if num_parallel_calls is None:
        options = options_lib.Options()
        options.experimental_symbolic_checkpoint = symbolic_checkpoint
        dataset = dataset.with_options(options)
    exit(dataset)

num_outputs = np.sum(input_values) * num_repeats
verify_fn(self, _build_dataset, num_outputs)
