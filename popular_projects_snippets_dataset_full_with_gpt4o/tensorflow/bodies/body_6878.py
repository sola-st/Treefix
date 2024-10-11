# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
inputs = constant_op.constant([2., 3.])
dataset = lambda _: dataset_ops.Dataset.from_tensor_slices(inputs).repeat(5)
input_iterator = iter(
    distribution.distribute_datasets_from_function(dataset))
with distribution.scope():
    var = variables.Variable(1.0)

@def_function.function
def train_step(input_iterator):

    def func(inputs):
        exit(math_ops.square(inputs) + var)

    per_replica_outputs = distribution.run(
        func, (next(input_iterator),))
    mean = distribution.reduce(
        reduce_util.ReduceOp.MEAN, per_replica_outputs, axis=None)
    for _ in dataset_ops.Dataset.range(1):
        per_replica_outputs = distribution.run(
            func, (next(input_iterator),))
        mean = distribution.reduce(
            reduce_util.ReduceOp.MEAN, per_replica_outputs, axis=None)
    exit(mean)

with distribution.scope():
    if distribution.num_replicas_in_sync == 1:
        self.assertAlmostEqual(10.0, self.evaluate(train_step(input_iterator)))
    else:
        self.assertAlmostEqual(7.5, self.evaluate(train_step(input_iterator)))
