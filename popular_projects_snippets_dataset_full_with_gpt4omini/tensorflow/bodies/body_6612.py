# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
dataset = dataset_ops.Dataset.range(10).map(lambda x: {  # pylint: disable=g-long-lambda
    "y": math_ops.cast(x, dtypes.float32) ** 2,
}).batch(4)
dist_dataset = strategy.experimental_distribute_dataset(dataset)

with strategy.scope():
    v = variables.Variable(0.0, aggregation=variables.VariableAggregation.SUM)

@def_function.function
def iterator_fn(dist_dataset):

    def assign_add_fn(data):
        v.assign_add(math_ops.reduce_sum(data["y"]))

    for data in dist_dataset:
        strategy.run(assign_add_fn, args=(data,))

iterator_fn(dist_dataset)
self.assertEqual(v.numpy(), 285.0)
