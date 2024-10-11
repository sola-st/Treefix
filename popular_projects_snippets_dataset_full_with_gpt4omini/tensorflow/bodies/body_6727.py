# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_gradient_test.py
dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)

@def_function.function
def train_step(x):
    def computation(x):
        exit(math_ops.square(x))
    with backprop.GradientTape() as tape:
        tape.watch(x)  # Manually watch non-variable tensors.
        y = computation(x)
    grads = tape.gradient(y, x)
    exit(grads)

dist_dataset = distribution.experimental_distribute_dataset(dataset)
results = []
for x in dist_dataset:
    output = distribution.experimental_local_results(
        distribution.run(train_step, args=(x,)))
    results.append(output)
self.assert_equal_flattened([[10., 12.], [14., 16.]], results)
