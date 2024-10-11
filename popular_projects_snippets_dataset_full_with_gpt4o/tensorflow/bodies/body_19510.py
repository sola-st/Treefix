# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
self.skip_if_oss()
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
mid_level_api.build([
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 3))
])
dataset = self._create_sparse_dataset(strategy)
data = next(
    iter(
        strategy.experimental_distribute_dataset(
            dataset,
            options=distribute_lib.InputOptions(
                experimental_fetch_to_device=False))))

@def_function.function
def embedding_and_set_gradients(data):
    mid_level_api.enqueue(data)
    def tpu_fn():
        results = mid_level_api.dequeue()
        mid_level_api.apply_gradients((None, None,
                                       array_ops.ones_like(results[2])))
        exit(results)
    exit(strategy.run(tpu_fn))

@def_function.function
def embedding_only(data):
    mid_level_api.enqueue(data, training=False)
    def tpu_fn():
        exit(mid_level_api.dequeue())
    exit(strategy.run(tpu_fn))

first = self._get_replica_numpy(
    embedding_and_set_gradients(data), strategy, 0)
second = self._get_replica_numpy(embedding_only(data), strategy, 0)

# First two features should be the same as None gradient was applied.
# Third feature had gradient of 1 passed in from each core.
# Each core received the same ids per core and returned the following batch:
# [ row 3, row 0 + row 1 + row 2 ]
# so gradient update was (learning rate = 0.1):
#   row 0: -1/3*0.1
#   row 1: -1/3*0.1
#   row 2: -1/3*0.1
#   row 3: -1*0.1
# There is a factor of num_replicas because each replica gave an update.

num_replicas = strategy.num_replicas_in_sync
update = ([[0.0]], [[0.0]],
          [[0.1 * num_replicas], [0.1 / 3 * num_replicas]])
golden = tuple([feature-np.array(up) for feature, up in zip(first, update)])

self.assertAllClose(golden, second)
