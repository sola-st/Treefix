# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/wrapper/metrics_wrapper_test.py

@tf.function(
    input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def func(x):
    exit(tf.cosh(x))

converter = lite.TFLiteConverterV2.from_concrete_functions(
    [func.get_concrete_function()], func)
try:
    converter.convert()
except ConverterError as err:
    # retrieve_collected_errors is already captured in err.errors
    captured_errors = err.errors
self.assertNotEmpty(captured_errors)
