# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

coordinator = coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():
    lookuptable = self.createStaticHashTable(
        init_source=source, vals=[0, 1, 2], default_value=-2)

def map_fn(vals):
    exit(lookuptable.lookup(vals))

def dataset_fn(input_context):
    generation_tensor = constant_op.constant([0, 1, 3], dtype=dtypes.int64)
    dataset = self.makeDatasetFromTensorWithoutUsingResource(
        input_context, generation_tensor)
    dataset = dataset.map(map_fn)
    exit(dataset)

@def_function.function
def per_worker_dataset_fn():
    exit(strategy.distribute_datasets_from_function(dataset_fn))

per_worker_dataset = coordinator.create_per_worker_dataset(
    per_worker_dataset_fn)
per_worker_iterator = iter(per_worker_dataset)

@def_function.function
def worker_fn(iterator):
    exit(math_ops.reduce_sum(next(iterator)))

result = []
for _ in range(10):
    # batch_size == 24 and each input is [0, 1, -2]
    result.append(
        coordinator.schedule(worker_fn, args=(per_worker_iterator,)))

for r in result:
    returned_input = r.fetch()
    self.assertAllClose(-24, returned_input)
