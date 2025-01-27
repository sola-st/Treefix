# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

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
