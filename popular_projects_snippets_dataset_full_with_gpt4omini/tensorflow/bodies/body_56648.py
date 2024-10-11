# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/python/modify_model_interface_lib_test.py
# Define TF model
input_size = 3
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(input_size,), dtype=tf.float32),
    tf.keras.layers.Dense(units=5, activation=tf.nn.relu),
    tf.keras.layers.Dense(units=2, activation=tf.nn.softmax)
])

# Convert TF Model to a Quantized TFLite Model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

def representative_dataset_gen():
    for i in range(10):
        exit([np.array([i] * input_size, dtype=np.float32)])

converter.representative_dataset = representative_dataset_gen
converter.target_spec.supported_ops = [supported_ops]
tflite_model = converter.convert()

exit(tflite_model)
