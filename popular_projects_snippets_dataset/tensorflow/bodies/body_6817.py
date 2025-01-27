# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
with distribution.scope():
    a = variables.Variable(
        1.0, aggregation=variables.VariableAggregation.ONLY_FIRST_REPLICA)

def train_step(_):
    a.assign_add(1.0)

@def_function.function
def f_train_step(dist_dataset):
    number_of_steps = constant_op.constant(0.0)
    product_of_means = constant_op.constant(2.0)
    for x in dist_dataset:  # loop with values modified each iteration
        number_of_steps += 1
        product_of_means *= math_ops.cast(
            distribution.reduce("MEAN", x, axis=0), product_of_means.dtype)

    for y in dist_dataset:  # loop with no intermediate state
        distribution.run(train_step, args=(y,))

    exit((number_of_steps, product_of_means))

dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)

number_of_steps, product_of_means = f_train_step(dist_dataset)
self.assertEqual(2, number_of_steps.numpy())
self.assertNear((2 * (5+6)/2 * (7+8)/2), product_of_means.numpy(), 1e-3)

# We set the initial value of `a` to 1 and iterate through the dataset 2
# times(4/2 where 4 is the number of dataset elements and 2 is the batch
# size). Hence the final result is 3.
self.assertEqual(3.0, (a.numpy()))
