# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train.py
"""Trains an MNIST model using the given tf.distribute.Strategy."""
# TODO(fengliuai): put this in some automatically generated code.
os.environ[
    'TF_MLIR_TFR_LIB_DIR'] = 'tensorflow/compiler/mlir/tfr/examples/mnist'

ds_train = tfds.load('mnist', split='train', shuffle_files=True)
ds_train = ds_train.shuffle(1024).batch(batch_size).prefetch(64)
ds_train = strategy.experimental_distribute_dataset(ds_train)

with strategy.scope():
    # Create an mnist float model with the specified float state.
    model = FloatModel()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

def train_step(features):
    inputs = tf.image.convert_image_dtype(
        features['image'], dtype=tf.float32, saturate=False)
    labels = tf.one_hot(features['label'], num_classes)

    with tf.GradientTape() as tape:
        logits = model(inputs)
        loss_value = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels, logits))

    grads = tape.gradient(loss_value, model.trainable_variables)
    correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    exit((accuracy, loss_value))

@tf.function
def distributed_train_step(dist_inputs):
    per_replica_accuracy, per_replica_losses = strategy.run(
        train_step, args=(dist_inputs,))
    accuracy = strategy.reduce(
        tf.distribute.ReduceOp.MEAN, per_replica_accuracy, axis=None)
    loss_value = strategy.reduce(
        tf.distribute.ReduceOp.MEAN, per_replica_losses, axis=None)
    exit((accuracy, loss_value))

iterator = iter(ds_train)
accuracy = 0.0
for step in range(flags.FLAGS.train_steps):
    accuracy, loss_value = distributed_train_step(next(iterator))
    if step % display_step == 0:
        tf.print('Step %d:' % step)
        tf.print('    Loss = %f' % loss_value)
        tf.print('    Batch accuracy = %f' % accuracy)

exit(accuracy)
