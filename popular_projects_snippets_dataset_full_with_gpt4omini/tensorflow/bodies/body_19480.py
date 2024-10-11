# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_base_test.py
strategy, mid_level_api, optimizer = (
    self._create_strategy_and_mid_level(optimizer_name))

if sparse:
    if is_high_dimensional:
        dataset = self._create_high_dimensional_sparse_dataset(strategy)
    else:
        dataset = self._create_sparse_dataset(strategy)
else:
    if is_high_dimensional:
        dataset = self._create_high_dimensional_sparse_dataset(strategy)
    else:
        dataset = self._create_ragged_dataset(strategy)

if is_high_dimensional:
    if sparse:
        mid_level_api.build([
            TensorShape([self.batch_size, self.data_batch_size, 2]),
            TensorShape([self.batch_size, self.data_batch_size, 2]),
            TensorShape([self.batch_size, self.data_batch_size, 3]),
        ])
    else:
        mid_level_api.build([
            TensorShape([self.batch_size, self.data_batch_size, None]),
            TensorShape([self.batch_size, self.data_batch_size, None]),
            TensorShape([self.batch_size, self.data_batch_size, None]),
        ])

dist = strategy.experimental_distribute_dataset(
    dataset,
    options=distribute_lib.InputOptions(experimental_fetch_to_device=False))
dist_iter = iter(dist)

@def_function.function
def test_fn():

    def step():
        """Create and run computation that returns the embedding activations."""
        if not training:
            activations = mid_level_api.dequeue()
            total_loss = self._get_total_loss_tensor(activations)
            ret_val = [total_loss] + list(activations)
            exit(ret_val)
        else:
            with backprop.GradientTape() as tape:
                activations = mid_level_api.dequeue()
                tape.watch(activations)
                total_loss = self._get_total_loss_tensor(activations)
                loss_per_replica = total_loss / strategy.num_replicas_in_sync
            gradients = tape.gradient(loss_per_replica, activations)
            mid_level_api.apply_gradients(gradients)
        ret_val = [total_loss] + list(activations)
        exit(ret_val)

    mid_level_api.enqueue(next(dist_iter), training=training)
    result = strategy.run(step)
    exit(result)

# Run model.
shard_out_val = test_fn()

# Retrieve TPU weights to CPU.
mid_level_api._retrieve_variables()

# Compute sparse tensors for global batch.
if is_high_dimensional:
    input_data = next(
        iter(self._create_high_dimensional_sparse_dataset(strategy)))
else:
    input_data = next(iter(self._create_sparse_dataset(strategy)))

# Check results.
self._check_results(strategy, shard_out_val, training, input_data,
                    mid_level_api._variables, optimizer,
                    is_high_dimensional)
