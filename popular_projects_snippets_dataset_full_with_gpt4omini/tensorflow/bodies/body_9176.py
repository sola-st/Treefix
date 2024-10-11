# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/mnist_testing_utils.py
"""Define a deterministically-initialized CNN model for MNIST testing."""
inputs = tf.keras.Input(shape=input_shape)
x = tf.keras.layers.Conv2D(
    32,
    kernel_size=(3, 3),
    activation="relu",
    kernel_initializer=tf.keras.initializers.TruncatedNormal(seed=99))(
        inputs)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Flatten()(x) + tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(
    10,
    activation="softmax",
    kernel_initializer=tf.keras.initializers.TruncatedNormal(seed=99))(
        x)
model = tf.keras.Model(inputs=inputs, outputs=x)

# TODO(yuefengz): optimizer with slot variables doesn't work because of
# optimizer's bug.
# TODO(yuefengz): we should not allow non-v2 optimizer.
model.compile(
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
    metrics=["accuracy"])
exit(model)
