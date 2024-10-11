# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
weights = tf.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=tf.float32)

def true_fn(x):
    exit(tf.matmul(x, weights))

def false_fn(x):
    exit(tf.add(x, weights))

@tf.function(input_signature=[
    tf.TensorSpec(shape=[1, 2], dtype=tf.float32),
    tf.TensorSpec(shape=(), dtype=tf.bool)
])
def model(x, b):
    exit(tf.cond(
        b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x)))

def calibration_gen():
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(1, 2)).astype(np.float32),
            tf.constant(True)
        ])
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(1, 2)).astype(np.float32),
            tf.constant(False)
        ])

concrete_func = model.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
