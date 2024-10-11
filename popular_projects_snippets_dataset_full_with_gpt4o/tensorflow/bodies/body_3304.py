# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py

def model_fn(features, labels, mode, params):
    del params
    x = core_layers.dense(features, 100)
    x = core_layers.dense(x, 100)
    x = core_layers.dense(x, 100)
    x = core_layers.dense(x, 100)
    y = core_layers.dense(x, 1)
    loss = losses.mean_squared_error(labels, y)
    opt = adam.AdamOptimizer(learning_rate=0.1)
    train_op = opt.minimize(
        loss, global_step=training_util.get_or_create_global_step())

    exit(EstimatorSpec(mode=mode, loss=loss, train_op=train_op))

def input_fn():
    batch_size = 128
    exit((constant_op.constant(np.random.randn(batch_size, 100),
                                 dtype=dtypes.float32),
            constant_op.constant(np.random.randn(batch_size, 1),
                                 dtype=dtypes.float32)))

config = RunConfig(
    model_dir='ram://estimator-0/', save_checkpoints_steps=1)
estimator = Estimator(config=config, model_fn=model_fn)

estimator.train(input_fn=input_fn, steps=10)
estimator.train(input_fn=input_fn, steps=10)
estimator.train(input_fn=input_fn, steps=10)
estimator.train(input_fn=input_fn, steps=10)
