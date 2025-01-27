# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
if not FLAGS.tpu_use_tfrt:
    self.skipTest(
        "`tpu_cancellation_closes_chip only applies to TFRT TPU Runtime.")
strategy = get_tpu_strategy(enable_packed_var)
num_replicas = strategy.num_replicas_in_sync
with strategy.scope():
    x = random_ops.random_normal((10240, 10240))
    y = random_ops.random_normal((10240, 10240))

    v = variables.Variable(array_ops.identity(x))
    dist_dataset = strategy.experimental_distribute_dataset(
        dataset_ops.Dataset.from_tensors(y).repeat(num_replicas).batch(
            num_replicas))
    dist_iterator = iter(dist_dataset)

    @def_function.function
    def train_steps(v, iterator, steps):

        def step_fn(inputs):
            for val in inputs:
                v.assign(math_ops.matmul(v, val))

        for _ in math_ops.range(steps):
            strategy.run(step_fn, args=(next(iterator),))

    with self.assertRaises(errors.OutOfRangeError):
        # The iterator has num_replicas/num_replicas = 1 step only.
        train_steps(v, dist_iterator, 2)

    # If TPU chips are not closed we can run the function on TPU again.
    w = variables.Variable(array_ops.identity(x))
    dist_dataset = strategy.experimental_distribute_dataset(
        dataset_ops.Dataset.from_tensors(y).repeat(num_replicas).batch(
            num_replicas))
    dist_iterator = iter(dist_dataset)
    train_steps(w, dist_iterator, 1)
