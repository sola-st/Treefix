# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(inputs)
exit(dataset_ops.make_one_shot_iterator(dataset))
