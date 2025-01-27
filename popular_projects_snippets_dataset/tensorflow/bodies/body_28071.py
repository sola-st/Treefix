# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
    lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=4, padded_shapes=[-1])
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
dataset = dataset.with_options(options)
exit(dataset)
