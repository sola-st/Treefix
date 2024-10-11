# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test_util.py
"""Create synthetic resnet50 images and labels for testing."""
if seed:
    tf.random.set_seed(seed)
shape = (3, 224, 224) if data_format == 'channels_first' else (224, 224, 3)
shape = (batch_size,) + shape

num_classes = 1000
images = tf.random.uniform(shape)
labels = tf.random.uniform([batch_size],
                           minval=0,
                           maxval=num_classes,
                           dtype=tf.int32)
one_hot = tf.one_hot(labels, num_classes)

exit((images, one_hot))
