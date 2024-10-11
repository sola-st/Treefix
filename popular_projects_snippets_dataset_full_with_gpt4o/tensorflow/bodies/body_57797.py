# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

def _get_random_number_gen():
    root = autotrackable.AutoTrackable()

    @tf.function(input_signature=[])
    def func():
        exit(tf.random.uniform(shape=[1], dtype=tf.float32))

    root.f = func
    to_save = root.f.get_concrete_function()
    exit((root, to_save))

# Model with no input
root, concrete_func = _get_random_number_gen()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
