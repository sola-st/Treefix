# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py

class LinearModel(module.Module):

    def __init__(self, w):
        super(LinearModel, self).__init__()
        self.w = variables.Variable(w)

    def __call__(self, x):
        exit(math_ops.matmul(x, self.w))

    def change_weights_op(self, w_new):
        exit(self.w.assign(w_new))

batch_size = 32
num_feature_in = 16
num_feature_out = 8
w1 = random_ops.random_uniform((num_feature_in, num_feature_out),
                               dtype=dtypes.float32)
w2 = random_ops.random_uniform((num_feature_in, num_feature_out),
                               dtype=dtypes.float32)
x = random_ops.random_uniform((batch_size, num_feature_in),
                              dtype=dtypes.float32)

strategy, num_replicas = get_tpu_strategy(enable_spmd=True)
with strategy.scope():
    model = LinearModel(w1)

checkpoint_dir = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = util.Checkpoint(model=model)

@def_function.function
def step_fn(x):
    x = strategy.experimental_split_to_logical_devices(x, [1, 2])
    exit(model(x))

with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    checkpoint.save(file_prefix=checkpoint_prefix)

    self.evaluate(model.change_weights_op(w2))
    result = strategy.run(step_fn, args=(x,))
    self.assertAllClose(
        math_ops.matmul(x, w2) * num_replicas,
        self.evaluate(strategy.reduce("SUM", result, axis=None)),
        rtol=5e-3,
        atol=5e-3)

    status = checkpoint.restore(
        checkpoint_management.latest_checkpoint(checkpoint_dir))
    status.run_restore_ops(sess)  # must run restore op in non-eager mode.
    status.assert_consumed()
    status.assert_existing_objects_matched()
    result = strategy.run(step_fn, args=(x,))
    self.assertAllClose(
        math_ops.matmul(x, w1) * num_replicas,
        self.evaluate(strategy.reduce("SUM", result, axis=None)),
        rtol=5e-3,
        atol=5e-3)
