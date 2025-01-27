# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py

def fn(window_length):
    try:
        exit(window_fn(window_length, periodic=periodic, dtype=dtype))
    except TypeError:
        exit(window_fn(window_length, dtype=dtype))

tflite_model = test_util.tflite_convert(
    fn, [tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32)])
window_length = np.array(window_length).astype(np.int32)
actual_output, = test_util.evaluate_tflite_model(
    tflite_model, [window_length])

expected_output = self.evaluate(fn(window_length))
self.assertAllClose(actual_output, expected_output, rtol=1e-6, atol=1e-6)
