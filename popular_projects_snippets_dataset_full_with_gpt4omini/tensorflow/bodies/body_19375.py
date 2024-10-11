# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
mid_level_api.build([
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 3))
])
dataset = self._create_sparse_dataset(strategy)
dataset_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def enqueue_with_no_gradient_apply(data):
    def get_activations(features):
        # Note the lack of setting training=False, so training defaults to true
        # here even though we don't have apply gradients.
        # We detect the correct mode based on which ops exist that share the
        # same 'name'.
        mid_level_api.enqueue(features, name='call1')
        exit(mid_level_api.dequeue(name='call1'))
    exit(strategy.run(get_activations, args=(data,)))

@def_function.function
def enqueue_with_gradient_apply(data):
    def get_activations(features):
        mid_level_api.enqueue(features, name='call2')
        activations = mid_level_api.dequeue(name='call2')
        # Apply an all ones gradient
        gradients = nest.map_structure(array_ops.ones_like, activations)
        mid_level_api.apply_gradients(gradients, name='call2')
        exit(activations)
    exit(strategy.run(get_activations, args=(data,)))

data = next(dataset_iter)
before_gradient_apply = enqueue_with_gradient_apply(data)
after_gradient_apply = enqueue_with_no_gradient_apply(data)
before_gradient_apply0 = self._get_replica_numpy(before_gradient_apply,
                                                 strategy, 0)
after_gradient_apply0 = self._get_replica_numpy(after_gradient_apply,
                                                strategy, 0)

num_replicas = strategy.num_replicas_in_sync
# We are passing a gradient of 1 for all lookups, optimizer is SGD with a
# learning rate of 0.1. Feature 0 and 1 are looked up with a sum combiner
# with the following ids:
# Feature 0: [0, 0, 1], [0, 1, 1], ... repeated over num_replicas
# Feature 1: [0, 1, 1], [0, 0, 1], ... repeated over num_replicas
# i.e. Row 0 and 1 were looked up 3*num_replicas times over all cores and as
# the gradient is 1, the accumulated gradient is 3*num_replicas for each
# position in row 0 and 1 in table.
#
# See comments in test_pass_none_to_apply_gradients for the update to
# Feature 2 and its table.
# The *2 in the next tests are because those rows have 2 lookups vs
# the 1 lookup in the other row.
update = ([[0.3 * num_replicas], [0.3 * num_replicas * 2]],
          [[0.3 * num_replicas * 2], [0.3 * num_replicas]],
          [[0.1 * num_replicas], [0.1 / 3 * num_replicas]])
golden = tuple([before - np.array(up) for before, up in
                zip(before_gradient_apply0, update)])

self.assertAllClose(golden, after_gradient_apply0)
