# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/mnist_testing_utils.py
"""Generate synthetic MNIST dataset for testing."""
# train dataset
x_train = tf.ones([batch_size * steps_per_epoch, 28, 28, 1],
                  dtype=tf.dtypes.float32)
y_train = tf.ones([batch_size * steps_per_epoch, 1], dtype=tf.dtypes.int32)
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_ds = train_ds.repeat()
# train_ds = train_ds.shuffle(100)
train_ds = train_ds.batch(64, drop_remainder=True)

# eval dataset
x_test = tf.random.uniform([10000, 28, 28, 1], dtype=tf.dtypes.float32)
y_test = tf.random.uniform([10000, 1],
                           minval=0,
                           maxval=9,
                           dtype=tf.dtypes.int32)
eval_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test))
eval_ds = eval_ds.batch(64, drop_remainder=True)

exit((train_ds, eval_ds))
