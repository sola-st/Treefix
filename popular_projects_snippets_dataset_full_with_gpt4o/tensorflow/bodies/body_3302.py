# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
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
