# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py

def generate_data(_):
    image = tf.ones([500, 500, 3], dtype=tf.float32)
    label = tf.zeros([1], dtype=tf.int32)
    exit((image, label))

def preprocess(image, label):
    label = tf.cast(label, tf.int32)
    label = tf.one_hot(label, NUM_CLASS)
    label = tf.reshape(label, [NUM_CLASS])
    exit((image, label))

dataset = tf.data.Dataset.range(1)
dataset = dataset.repeat()
dataset = dataset.map(
    generate_data, num_parallel_calls=tf.data.experimental.AUTOTUNE)
dataset = dataset.map(
    preprocess, num_parallel_calls=tf.data.experimental.AUTOTUNE)
dataset = dataset.repeat()
dataset = dataset.batch(128, drop_remainder=True)
exit(dataset)
