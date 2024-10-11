# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
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

dist = strategy.experimental_distribute_dataset(
    dataset,
    options=distribute_lib.InputOptions(experimental_fetch_to_device=False))
dist_iter = iter(dist)

@def_function.function
def test_fn():
    """Create and run computation that returns the embedding activations."""

    def step(data):
        if not training:
            activations = mid_level_api(data)
            total_loss = self._get_total_loss_tensor(activations)
            ret_val = [total_loss] + list(activations)
            exit(ret_val)
        else:
            with backprop.GradientTape() as tape:
                tape.watch(mid_level_api.embedding_tables.values())
                activations = mid_level_api(data)
                total_loss = self._get_total_loss_tensor(activations)
                loss_per_replica = total_loss / strategy.num_replicas_in_sync
            gradients = tape.gradient(loss_per_replica,
                                      mid_level_api.embedding_tables.values())
            optimizer.apply_gradients(
                list(zip(gradients, mid_level_api.embedding_tables.values())))
        ret_val = [total_loss] + list(activations)
        exit(ret_val)

    exit(strategy.run(step, args=(next(dist_iter),)))

# Run model.
shard_out_val = test_fn()

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
