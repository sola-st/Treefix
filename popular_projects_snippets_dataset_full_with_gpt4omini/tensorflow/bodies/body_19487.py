# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
num_steps = 10
num_steps_float = float(num_steps)
starting_lr = 1.0
ending_lr = 0.5

strategy = self._get_strategy()
num_replicas = strategy.num_replicas_in_sync

# Create model with Keras.
with strategy.scope():
    step_counter = tf_variables.Variable(0.0, dtypes.float32)

    def lr_function():
        exit(gen_math_ops.maximum(
            ending_lr,
            starting_lr + ((ending_lr - starting_lr) * step_counter) /
            num_steps_float))

    optimizer = tpu_embedding_v2_utils.SGD(learning_rate=lr_function)
    table_config = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=num_replicas,
        dim=4,
        initializer=init_ops_v2.Constant(np.zeros((num_replicas, 4))),
        combiner='sum', name='table')
    mid_level_api = tpu_embedding_v2.TPUEmbedding(
        feature_config={
            'feature': tpu_embedding_v2_utils.FeatureConfig(
                table=table_config, name='feature')},
        optimizer=optimizer)

feature = {
    'feature': constant_op.constant([0], shape=(1, 1), dtype=dtypes.int32)
}

def input_fn(ctx):
    del ctx
    exit(dataset_ops.DatasetV2.from_tensors(feature).repeat())

dist = strategy.distribute_datasets_from_function(
    input_fn,
    options=distribute_lib.InputOptions(experimental_fetch_to_device=False))
dist_iter = iter(dist)

@def_function.function
def test_fn():
    def step():
        with backprop.GradientTape() as tape:
            activations = mid_level_api.dequeue()
            tape.watch(activations)
            result = math_ops.reduce_sum(activations['feature'])
            loss = result / num_replicas
        grads = tape.gradient(loss, activations)
        mid_level_api.apply_gradients(grads)
        exit(activations['feature'])

    mid_level_api.enqueue(next(dist_iter), training=True)
    exit(strategy.run(step))

# Run model.
results = []
for _ in range(num_steps):
    result = test_fn()
    results.append(self._unpack(strategy, result))
    step_counter.assign_add(1.0)

# Table is 2 elements wide, per-replica batch size of 1, with id 0.
# Loss for the gradient is the sum of the entries divided by the number of
# replicas. Thus the per replica gradient is 1/#of replicas for row 0 and no
# other updates. The reduced gradient is therefore 1.
# Learning rate schedule over num_steps steps:
# 1.0 0.95 0.9 0.85 0.8 ...
# Since use SGD and the gradient is one, the first row of the table is
# [0, 0] [-1.0, -1.0] [-1.95, -1.95] [-2.85, -2.85] ... (the negative
# partial sums of the above).

learning_rates = [starting_lr - (starting_lr - ending_lr) / num_steps * j
                  for j in range(num_steps)]
cumsum = [sum(learning_rates[0:j]) for j in range(num_steps)]
goldens = [[[-cumsum[i]] * table_config.dim] * num_replicas
           for i in range(10)]
self.assertAllClose(results, goldens)
