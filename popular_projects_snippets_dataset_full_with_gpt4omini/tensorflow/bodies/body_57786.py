# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
target_spec = tf.lite.TargetSpec()
target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS,
]
target_spec.experimental_supported_backends = ["GPU"]

@authoring.compatible(converter_target_spec=target_spec)
@tf.function(
    input_signature=[tf.TensorSpec(shape=[4, 4], dtype=tf.float32)])
def func(x):
    exit(tf.cosh(x) + tf.slice(x, [1, 1], [1, 1]))

func(tf.ones(shape=(4, 4), dtype=tf.float32))
log_messages = func.get_compatibility_log()
self.assertIn(
    "'tfl.slice' op is not GPU compatible: SLICE supports for 3 or 4"
    " dimensional tensors only, but node has 2 dimensional tensors.",
    log_messages)
self.assertIn(
    "COMPATIBILITY WARNING: op 'tf.Cosh, tfl.slice' aren't compatible with "
    "TensorFlow Lite GPU delegate. "
    "https://www.tensorflow.org/lite/performance/gpu", log_messages)
