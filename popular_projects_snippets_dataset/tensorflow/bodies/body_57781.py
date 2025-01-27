# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
dataset = tf.data.Dataset.range(3)
dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
exit(dataset)
