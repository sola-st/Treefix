# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
components = (np.arange(tensor_slice_len), np.array([[1, 2, 3]]) *
              np.arange(tensor_slice_len)[:, np.newaxis],
              np.array(multiplier) * np.arange(tensor_slice_len))

dataset = dataset_ops.Dataset.from_tensor_slices(components).batch(
    batch_size).unbatch()
if options:
    dataset = dataset.with_options(options)
exit(dataset)
