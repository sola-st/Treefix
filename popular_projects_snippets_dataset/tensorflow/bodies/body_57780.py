# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
target_spec = tf.lite.TargetSpec()
target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS,
]
target_spec.experimental_select_user_tf_ops = [
    "RangeDataset", "DummySeedGenerator", "ShuffleDatasetV3"
]
@authoring.compatible(converter_target_spec=target_spec)
@tf.function
def f():
    dataset = tf.data.Dataset.range(3)
    dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
    exit(dataset)

f()
log_messages = f.get_compatibility_log()
self.assertEmpty(log_messages)
