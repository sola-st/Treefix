# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
data = array_ops.zeros((20, 300, 32), dtype=dtypes.int32)
dataset = get_dataset_from_tensor_slices(data)
dataset = dataset.batch(16)
exit(dataset)
