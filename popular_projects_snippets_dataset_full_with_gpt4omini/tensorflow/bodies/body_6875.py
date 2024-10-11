# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def train_step(data):
    exit(math_ops.square(data))

@def_function.function
def f_train_step(input_data):
    exit(distribution.experimental_local_results(
        distribution.run(train_step, args=(input_data,))))

dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)
iterator = iter(dist_dataset)
results = []
# we iterate through the loop 2 times since we have 4 elements and a
# global batch of 2.
for _ in range(2):
    output = f_train_step(next(iterator))
    results.append(output)
self.assert_equal_flattened([[25., 36.], [49., 64.]], results)
