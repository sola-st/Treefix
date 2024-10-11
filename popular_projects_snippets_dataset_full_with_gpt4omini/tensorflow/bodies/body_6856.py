# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset1 = get_dataset_from_tensor_slices([[1., 2.], [1., 2.]])
dataset2 = get_dataset_from_tensor_slices([[1., 2., 3.],
                                           [1., 2., 3.]])
dataset = dataset1.concatenate(dataset2)
dataset = dataset.batch(2, drop_remainder=True)
exit(dataset)
