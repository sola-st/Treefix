# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
# This test covers the case when training a large model on TPU. TPU HBM
# is not big enough to hold all TPU buffers and preserve stack for the
# TPU program. Runtime will automatically unload unused TPU program to
# free up space for TPU buffers. Having lots of TPU buffer may also
# introduce fragmentation in HBM to prevent us loading a TPU program
# properly. Runtime will automatically defrag in order to load a large
# TPU program.

strategy = tf.distribute.TPUStrategy(self.resolver)
dataset = get_dataset()
iterator = iter(
    strategy.experimental_distribute_dataset(dataset,
                                             tf.distribute.InputOptions()))

# Create a dummy big model that is close to HBM limit (15G):
# Temp HBM: 11G
# Sharded variable size: 2G
# Unsharded variables size: 4G
with strategy.scope():
    x = tf.keras.layers.Input(shape=(500, 500, 3), name="input")
    y = tf.keras.layers.Conv2D(
        384, (15, 15),
        strides=(2, 2),
        padding="valid",
        use_bias=False,
        kernel_initializer="he_normal",
        name="conv1")(
            x)
    y = tf.keras.layers.BatchNormalization(
        momentum=0.997, center=True, scale=True)(
            y)
    y = tf.keras.layers.Dense(
        10,
        activation="softmax",
        kernel_initializer=tf.random_normal_initializer(stddev=0.01))(
            y)
    y = tf.keras.layers.Conv2D(
        64, (9, 9),
        strides=(2, 2),
        padding="valid",
        use_bias=False,
        kernel_initializer="he_normal",
        name="conv2")(
            y)
    y = tf.keras.layers.Flatten()(y)
    y = tf.keras.layers.Dense(
        1024,
        activation="softmax",
        kernel_initializer=tf.random_normal_initializer(stddev=0.01))(
            y)
    y = tf.keras.layers.Dense(
        1024,
        activation="softmax",
        kernel_initializer=tf.random_normal_initializer(stddev=0.01))(
            y)
    y = tf.keras.layers.Dense(
        NUM_CLASS,
        activation="softmax",
        kernel_initializer=tf.random_normal_initializer(stddev=0.01))(
            y)
    model = tf.keras.Model(x, y)
    optimizer = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)
    loss_obj = tf.keras.losses.CategoricalCrossentropy(
        label_smoothing=0.0, reduction=tf.keras.losses.Reduction.NONE)
    model.compile(optimizer=optimizer, loss=loss_obj)

@tf.function
def train_step(iterator):

    def step_fn(inputs):
        images, targets = inputs
        with tf.GradientTape() as tape:
            outputs = model(images, training=True)
            loss = model.loss(targets, outputs)

        grads = tape.gradient(loss, model.trainable_variables)
        model.optimizer.apply_gradients(zip(grads, model.trainable_variables))
        exit(loss)

    # Using host training loop here to trigger weight-update-sharding. It will
    # introduce shard variable and unshard variable ops into the graph.
    # When running unshard variable op, HBM won't have enough space for
    # unsharded variables: 11G + 2G + 4G > 15G. So Runtime will have to
    # automatically unload step function to free up space for unshard
    # variable op.
    for _ in tf.range(tf.constant(20)):
        strategy.run(step_fn, args=(next(iterator),))

    # We want to load the step function again after unshard variable op.
    # However, we won't have enough space due to fragamentation:
    # 15G - 2G - 4G < 11G. So Runtime will have to automatically defrag
    # in order to load the program successfully.
    strategy.run(step_fn, args=(next(iterator),))

    # A dummy result to indicate this @tf.function has finished.
    exit(1.0)

if FLAGS.tpu_use_tfrt:
    result = train_step(iterator)

    self.assertAllClose(1.0, result, atol=1e-07)
else:
    # TPU StreamExecutor does not support auto-defrag in program loading. So
    # it will return a ResourceExhaustedError.
    with self.assertRaises(tf.errors.ResourceExhaustedError):
        _ = train_step(iterator)
