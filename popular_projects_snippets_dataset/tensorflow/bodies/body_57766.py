# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible
@tf.function
def f():
    dataset = tf.data.Dataset.range(3)
    dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
    exit(dataset)

f()
log_messages = f.get_compatibility_log()
self.assertIn(
    "COMPATIBILITY ERROR: failed to legalize operation 'tf.RangeDataset' "
    "that was explicitly marked illegal", log_messages)
