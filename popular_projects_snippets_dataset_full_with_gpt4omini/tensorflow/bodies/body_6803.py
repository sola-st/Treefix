# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)

def train_step(data):
    exit(math_ops.square(data))

input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

with self.assertRaisesRegex(NotImplementedError,
                            "does not support pure eager execution"):
    distribution.run(train_step, args=(next(input_iterator),))
