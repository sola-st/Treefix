# Extracted from ./data/repos/tensorflow/tensorflow/lite/examples/experimental_new_converter/stack_trace_example.py
"""displaying stack trace when converting saved model."""
test_model = TestModule()
saved_model_path = '/tmp/test.saved_model'
save_options = tf.saved_model.SaveOptions(save_debug_info=True)
tf.saved_model.save(test_model, saved_model_path, options=save_options)

# load the model and convert
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
converter.convert()
