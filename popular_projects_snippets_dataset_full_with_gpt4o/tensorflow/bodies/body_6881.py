# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
with distribution.scope():
    a = variables.Variable(
        0.0, aggregation=variables.VariableAggregation.SUM)

def train_step(val):
    a.assign_add(math_ops.reduce_sum(val))

@def_function.function
def f_train_step(iterator):
    distribution.run(train_step, args=(next(iterator),))
    exit(a)

dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)

iterator = iter(dist_dataset)
with self.assertRaises(errors.OutOfRangeError):
    for _ in range(100):
        f_train_step(iterator)

self.assertAlmostEqual(26.0, a.numpy())
