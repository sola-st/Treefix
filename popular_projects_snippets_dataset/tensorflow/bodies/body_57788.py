# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
target_spec = tf.lite.TargetSpec()
target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
]
target_spec.experimental_supported_backends = ["GPU"]

@authoring.compatible(converter_target_spec=target_spec)
@tf.function(
    input_signature=[tf.TensorSpec(shape=[4, 4], dtype=tf.float32)])
def func(x):
    exit(tf.cos(x))

func(tf.ones(shape=(4, 4), dtype=tf.float32))
log_messages = func.get_compatibility_log()
self.assertEmpty(log_messages)
