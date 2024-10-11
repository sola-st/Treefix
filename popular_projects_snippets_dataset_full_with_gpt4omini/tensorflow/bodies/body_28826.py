# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
dataset = dataset_ops.Dataset.from_tensors(1).repeat(num_elements)
dataset = dataset.scan(
    initial_state=[0, 1],
    scan_func=lambda a, _: ([a[1], a[0] + a[1]], a[1]))
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
exit(dataset.with_options(options))
